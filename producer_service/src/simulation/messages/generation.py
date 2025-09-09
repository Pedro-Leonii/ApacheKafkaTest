from abc import ABC, abstractmethod
import random
from datetime import datetime

import simulation.messages.data as data
from simulation.messages.content import Severity, HttpMethod


class IMetricGenerationStrategy(ABC):
    
    @abstractmethod
    def get_metrics(self) -> dict:
        ...
    
class MetricsRandomGeneration(IMetricGenerationStrategy):

    def get_metrics(self) -> dict:
        return {
            "cpu": random.randint(30, 95),
            "threads": random.randint(1,40),
            "users": random.randint(0,1500),
            "datetime": datetime.now(),
            "open_files": random.randint(0,10)
        }
    
class IApplicationLogGenerationStrategy(ABC):

    @abstractmethod
    def generate_log(self) -> dict:
        ...
    
class ApplicationLogRandomGeneration(IApplicationLogGenerationStrategy):

    def generate_log(self) -> dict:
        return {
            "datetime": datetime.now(),
            "severity": random.choice(list(Severity)),
            "msg": random.choice(data.MSGS),
            "thread": random.choice(data.THREADS),
            "cls": random.choice(data.CLSES),
        }
    
class IAccessLogGenerationStrategy(ABC):

    @abstractmethod
    def generate_log(self) -> dict:
        ...

class AccessLogRandomGeneration(IAccessLogGenerationStrategy):

    def generate_log(self) -> dict:
        return {
            "datetime": datetime.now(),
            "ip": f"192.68.{random.randint(0,255)}.{random.randint(1,254)}",
            "user": random.choice(data.USERS),
            "status_code": random.choice(data.STATUS_CODES),
            "dim": random.randint(500, 500_000),
            "url": random.choice(data.URLS),
            "uagent": random.choice(data.USER_AGENTS),
            "method": random.choice(list(HttpMethod))
        }