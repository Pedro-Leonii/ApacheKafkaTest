from threading import Thread, Event

from simulation.runner.runners import LogRunner, MetricsRunner
from simulation.serialization.serializers_factory import AvroSerializerFactory
from simulation.config.cfg import INTERVAL_METRICS, LAMBDA_LOGS, NODE_ID_LIST

def main():

    end_event: Event = Event()

    print(f"Inizio simulazione con {len(NODE_ID_LIST)} nodi...")
    

    serializer_factory: AvroSerializerFactory = AvroSerializerFactory()

    runners: list[Thread] = []
    for NODE_ID in NODE_ID_LIST:
        runners.append(LogRunner(end_event, LAMBDA_LOGS, serializer_factory, NODE_ID))
        runners.append(MetricsRunner(end_event, INTERVAL_METRICS, serializer_factory, NODE_ID))

    for runner in runners:
        runner.start()

    inp: str = ""

    while inp.strip().lower() != "q":
        inp = input("Premere Q/q per terminare la simulazione:")
    
    print("Termino nodi...")
    end_event.set()
    for runner in runners:
        runner.join()
