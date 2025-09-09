from abc import ABC, abstractmethod

from simulation.messages.content import ISendable, Metrics, AppLog, AccessLog
from simulation.messages.generation import IMetricGenerationStrategy, IApplicationLogGenerationStrategy, IAccessLogGenerationStrategy

class ISendableFactory(ABC):

    @abstractmethod
    def create(self) -> ISendable:
        ...

class MetricsFactory(ISendableFactory):

    def __init__(self, metrics_generator: IMetricGenerationStrategy):
        self._metrics_generator = metrics_generator

    def create(self) -> Metrics:
        metrics: dict = self._metrics_generator.get_metrics()

        return Metrics(
            cpu=metrics["cpu"],
            threads=metrics["threads"],
            users=metrics["users"],
            datetime=metrics["datetime"],
            open_files=metrics["open_files"]
        )



class AppLogFactory(ISendableFactory):

    def __init__(self, log_generator: IApplicationLogGenerationStrategy):
        self._log_generator = log_generator


    def create(self) -> AppLog:

        log: dict = self._log_generator.generate_log()

        return AppLog(
            datetime = log["datetime"],
            severity = log["severity"],
            msg = log["msg"],
            thread = log["thread"],
            cls = log["cls"]
        )

class AccessLogFactory(ISendableFactory):

    def __init__(self, log_generator: IAccessLogGenerationStrategy):
        self._log_generator = log_generator

    def create(self) -> AppLog:
        
        log: dict = self._log_generator.generate_log()

        return AccessLog(
            datetime = log["datetime"],
            ip = log["ip"],
            user = log["user"],
            status_code = log["status_code"],
            dim = log["dim"],
            url = log["url"],
            uagent = log["uagent"],
            method = log["method"]
        )
    

