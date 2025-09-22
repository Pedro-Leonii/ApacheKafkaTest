import random 
from datetime import datetime
from abc import ABC, abstractmethod

from simulation.core.messages import BaseMessage, ApplicationLogMessage, AccessLogMessage, ServerMetricsMessage
import simulation.generation.data as data

class MessageGenerationStrategy(ABC):
    @abstractmethod
    def generate(self, server_id:str) -> BaseMessage:
        ...

class ApplicationLogRandomGeneration(MessageGenerationStrategy):

    def generate(self, server_id: str) -> ApplicationLogMessage:
        return ApplicationLogMessage(
            server_id=server_id,
            generation_time=datetime.now(),
            severity=random.choice(data.SEVERITY),
            msg=random.choice(data.MSGS),
            source_thread=random.choice(data.THREADS),
            source_cls=random.choice(data.CLSES)
        )

class AccessLogRandomGeneration(MessageGenerationStrategy):

    def generate(self, server_id: str) -> AccessLogMessage:
        return AccessLogMessage(
            server_id=server_id,
            generation_time=datetime.now(),
            request_method=random.choice(data.METHODS),
            user_ip=f"192.68.{random.randint(0,255)}.{random.randint(1,254)}",
            username=random.choice(data.USERS),
            response_status_code=random.choice(data.STATUS_CODES),
            response_dim=random.randint(500, 500_000),
            request_url=random.choice(data.URLS),
            user_agent=random.choice(data.USER_AGENTS)
        )

class ServerMetricsRandomGeneration(MessageGenerationStrategy):

    def generate(self, server_id: str) -> ServerMetricsMessage:
        return ServerMetricsMessage(
            server_id=server_id,
            generation_time=datetime.now(),
            cpu_usage=random.randint(30, 95),
            running_threads=random.randint(1, 30),
            current_users=random.randint(0,1500),
            open_files=random.randint(0,10)
        )
