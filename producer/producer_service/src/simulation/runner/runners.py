import time
import random
from threading import Thread, Event

import scipy.stats as sts
from simulation.sender.sender import Sender

class LogRunner(Thread):

    def __init__(self, stop_event: Event, l:float, access_log_sender: Sender, application_log_sender: Sender):
        super().__init__()
        self._distr = sts.expon(scale=1/l)
        self._stop_event: Event = stop_event

        self._access_log_sender: Sender = access_log_sender
        self._application_log_sender: Sender = application_log_sender

    def run(self):
        while not self._stop_event.is_set():
            time.sleep(self._distr.rvs())
            self._access_log_sender.produce()
            self._application_log_sender.produce(random.randint(1,3))



class MetricsRunner(Thread):

    def __init__(self, stop_event: Event, t: int, metrics_sender: Sender):
        super().__init__()
        self._t = t
        self._stop_event: Event = stop_event
        self._metrics_producer: Sender = metrics_sender 

    def run(self):
        while not self._stop_event.is_set():
            time.sleep(self._t)
            self._metrics_producer.produce()