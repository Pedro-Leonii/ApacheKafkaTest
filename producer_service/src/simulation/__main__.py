import time
import random
from threading import Thread, Event, Lock

import scipy.stats as sts  

from simulation.producers.producers import Producer, ProducerResults
from simulation.producers.creation import ProducerFactory

end_event: Event = Event()

results_lock: Lock = Lock()
results: list[ProducerResults] = []

def simulate_logs_generation(l: float) -> None:

    access_log_producer: Producer = ProducerFactory.create_access_log_producer()
    app_log_producer: Producer = ProducerFactory.create_application_log_producer()

    Exp = sts.expon(scale=1/l)

    while(not end_event.is_set()):     
        t: float = Exp.rvs()
        time.sleep(t*60)
        access_log_producer.produce(1)
        app_log_producer.produce(random.randint(1,5))

    app_log_producer.cleen_up()
    access_log_producer.cleen_up()
    print("termino invio logs...")
    
    with results_lock as _:
        results.append(app_log_producer.results)
        results.append(access_log_producer.results)
    

def simulate_metrics_generation(t: int) -> None:

    metrics_producer: Producer = ProducerFactory.create_metrics_producer()

    while(not end_event.is_set()):
        metrics_producer.produce(1)
        time.sleep(t)

    metrics_producer.cleen_up()
    print("termino invio metriche...")

    with results_lock as _:
        results.append(metrics_producer.results)

def main():

    print(""" 
    ##################################
    #      INIZIO SIMULAZIONE...     #
    ##################################
    """)
    
    time.sleep(1)


    th_logs = Thread(target=simulate_logs_generation, args=(100, ))
    th_metrics = Thread(target=simulate_metrics_generation, args=(3,))

    th_logs.start()
    th_metrics.start()

    inp: str = ""


    while inp.capitalize() != "Q":
        inp = input("Premere Q/q per terminare la simulazione:")
    
    end_event.set()
    th_logs.join()
    th_metrics.join()

    for r in results:
        print("-------------------------------------------")
        print(f"Topic {r.topic}")
        print(f"Messaggi inviati correttamente: {r.n_sended}")
        print(f"Messaggi non inviati correttamente: {r.n_errors}")
        print("-------------------------------------------")
    





