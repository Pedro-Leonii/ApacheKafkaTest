import time
from threading import Event

from simulation.runner.runners import LogRunner, MetricsRunner
from simulation.serialization.serializers_factory import AvroSerializerFactory


def main():
    end_event: Event = Event()

    print(""" 
    ##################################
    #      INIZIO SIMULAZIONE...     #
    ##################################
    """)
    
    time.sleep(1)

    serializer_factory: AvroSerializerFactory = AvroSerializerFactory()

    th_logs = LogRunner(end_event, 100, serializer_factory)
    th_metrics = MetricsRunner(end_event, 1, serializer_factory)

    th_logs.start()
    th_metrics.start()

    inp: str = ""


    while inp.capitalize() != "Q":
        inp = input("Premere Q/q per terminare la simulazione:")
    
    end_event.set()
    th_logs.join()
    th_metrics.join()





