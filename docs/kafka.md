
## Organizzazione cluster Kafka
- Composto da tre nodi dato che si tratta di un PoC, inoltre così è possibile poter eventualmente stoppare un nodo senza bloccare l'intero cluster a causa dell'impossibilità di raggiungere il consenso.
- Per semplicità di gestione ogni nodo del cluster assume ruolo di broker e di controller, l'appesantimento dei nodi è trascurabile.

## Organizzazione producer
- I producer sono idem-potenti (ACKS=all e idempotence=True) perchè si vogliono poter eseguire algoritmi sul flusso di dati quindi è necessario avere delle certezze in termini di ordine di arrivo dei messaggi, singola ricezione dei messaggi e garanzia di arrivo.


## Organizzazione topic 
- Ogni tipo di dato trasmesso ha un proprio topic.
- Ogni istanza del servizio trasmette le informazioni usando il topic adeguato e usando il proprio identificativo come chiave dei messaggi.

Questo permette l'aggregazione dei dati in modo significativo da parte del sink connector, inoltre permette di parallelizzare il consumo dei dati sulla base del numero di servizi.

- Ogni istanza del servizio trasmette periodicamente le seguenti informazioni:
    - log degli accessi, log applicativo e del database.
    - insieme di dati telemetrici (% CPU, thread attivi, file aperti, numero utenti).

Quindi ogni topic deve avere almeno una partizione, per permettere il test usando più producer vengono utilizzate dodici partizioni che solitamente è il numero minimo consigliato per permettere sviluppi fututi, inoltre essendo un numero divisibile per il numero di broker permette di bilanciare il carico dei leader.

- Ogni topic ha un replication factor pari a 3 e numero minimo di repliche in sync pari a 2.

Questo permette di rendere la simulazione più realistica, andando a valutare le prestazioni su un esempio semplificato che però dà garanzie di durabilità e disponibilità appropriate.
Inoltre utilizzando il numero minimo di repliche in sync è possibile stoppare un broker senza compromettere il funzionamento del cluster.

Topic definiti:
- server.metrics
- server.logs.application
- server.logs.access
- server.logs.db

## Schemi dei messaggi
Per semplicità non viene utilizzato uno schema registry, invece sono i producer che impongono lo schema utilizzando JSON.
