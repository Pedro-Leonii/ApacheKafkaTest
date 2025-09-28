from abc import ABC, abstractmethod
import time 
import random

import scipy.stats as sts

from simulation.producer.producer import ProducerFacade
from simulation.send.factory import ApplicationLogSendRequestFactory, AccessLogSendRequestFactory, ServerMetricsRequestFactory
from simulation.runner import cfg

class ISimulationLogic(ABC):

    @abstractmethod
    def exec(self) -> None:
        raise NotImplementedError()
    
class LoggerSimulationLogic(ISimulationLogic):

    def __init__(self):
        self._access_log_send_req_factory = AccessLogSendRequestFactory()
        self._app_log_send_req_factory = ApplicationLogSendRequestFactory()
        self._distr = sts.expon(scale=1/cfg.LAMBDA_LOGS)

    def exec(self) -> None:
        time.sleep(self._distr.rvs())
        ProducerFacade.produce(
            self._access_log_send_req_factory.generate_send_request()
        )

        for _ in range(random.randint(1,3)):
            ProducerFacade.produce(
                self._app_log_send_req_factory.generate_send_request()
            )

class SystemMonitorSimulationLogic(ISimulationLogic):

    def __init__(self):
        self._server_metrics_request_factory = ServerMetricsRequestFactory()

    def exec(self) -> None:
        time.sleep(cfg.INTERVAL_METRICS)
        ProducerFacade.produce(
            self._server_metrics_request_factory.generate_send_request()
        )