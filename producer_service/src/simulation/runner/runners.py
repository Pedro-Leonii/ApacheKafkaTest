from threading import Thread, Event
import time
import random

import scipy.stats as sts

from simulation.config.cfg import NODE_ID, LAMBDA_LOGS, INTERVAL_METRICS
from simulation.sender.sender import Sender
from simulation.sender.senders_factory import SenderFactory
from simulation.serialization.serializers_factory import ISerializerFactory


class LogRunner(Thread):

    def __init__(self, stop_event: Event, l:float, serializer_factory: ISerializerFactory):
        super().__init__()
        self._distr = sts.expon(scale=1/l)
        self._stop_event: Event = stop_event

        self._access_log_sender: Sender = SenderFactory.create_access_log_sender(source=NODE_ID, serializer_factory=serializer_factory)

        self._application_log_sender: Sender = SenderFactory.create_app_log_sender(source=NODE_ID, serializer_factory=serializer_factory)
        

    def run(self):
        while not self._stop_event.is_set():
            time.sleep(self._distr.rvs() * 60)
            self._access_log_sender.produce()
            self._application_log_sender.produce(random.randint(1,3))

        self._access_log_sender.clean_up()
        self._application_log_sender.clean_up()
        print("termino invio logs...")




class MetricsRunner(Thread):

    def __init__(self, stop_event: Event, t: int, serializer_factory: ISerializerFactory):
        super().__init__()
        self._t = t
        self._stop_event: Event = stop_event
        self._metrics_producer: Sender = SenderFactory.create_metrics_sender(source=NODE_ID, serializer_factory=serializer_factory)
        

    def run(self):
        while not self._stop_event.is_set():
            time.sleep(self._t)
            self._metrics_producer.produce()

        self._metrics_producer.clean_up()
        print("termino invio metriche...")
    

