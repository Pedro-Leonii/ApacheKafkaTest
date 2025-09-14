import time
from threading import Event

from simulation.runner.runners import LogRunner, MetricsRunner
from simulation.result.writer import ResultWriterSingleton
from simulation.serialization.serializers_factory import AvroSerializerFactory
from simulation.config.cfg import INTERVAL_METRICS, LAMBDA_LOGS


def main():

    end_event: Event = Event()

    print(""" 
##################################
#      INIZIO SIMULAZIONE...     #
##################################
    """)
    

    serializer_factory: AvroSerializerFactory = AvroSerializerFactory()
    
    

    th_logs = LogRunner(end_event, LAMBDA_LOGS, serializer_factory)
    th_metrics = MetricsRunner(end_event, INTERVAL_METRICS, serializer_factory)

    th_logs.start()
    th_metrics.start()

    inp: str = ""


    while inp.capitalize() != "Q":
        inp = input("Premere Q/q per terminare la simulazione:")
    
    end_event.set()

    th_logs.join()
    th_metrics.join()
 





