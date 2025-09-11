import random 
from datetime import datetime

from abc import ABC, abstractmethod

from simulation.core.messages import BaseMessage, ApplicationLogMessage, AccessLogMessage, ServerMetricsMessage
import simulation.generation.data as data


class MessageGenerationStrategy(ABC):
    
    @property
    def source(self) -> str:
        return self._source

    @abstractmethod
    def generate(self, source:str) -> BaseMessage:
        ...


class ApplicationLogRandomGeneration(MessageGenerationStrategy):

    def generate(self, source: str) -> ApplicationLogMessage:
        return ApplicationLogMessage(
            source=source,
            datetime=datetime.now(),
            severity=random.choice(data.SEVERITY),
            msg=random.choice(data.MSGS),
            thread=random.choice(data.THREADS),
            cls=random.choice(data.CLSES)
        )

class AccessLogRandomGeneration(MessageGenerationStrategy):

    def generate(self, source: str) -> AccessLogMessage:
        return AccessLogMessage(
            source=source,
            datetime=datetime.now(),
            method=random.choice(data.METHODS),
            ip=f"192.68.{random.randint(0,255)}.{random.randint(1,254)}",
            user=random.choice(data.USERS),
            status_code=random.choice(data.STATUS_CODES),
            dim=random.randint(500, 500_000),
            url=random.choice(data.URLS),
            user_agent=random.choice(data.USER_AGENTS)
        )


class ServerMetricsRandomGeneration(MessageGenerationStrategy):

    def generate(self, source: str) -> ServerMetricsMessage:
        return ServerMetricsMessage(
            source=source,
            datetime=datetime.now(),
            cpu=random.randint(30, 95),
            threads=random.randint(1, 30),
            users=random.randint(0,1500),
            open_files=random.randint(0,10)
        )
