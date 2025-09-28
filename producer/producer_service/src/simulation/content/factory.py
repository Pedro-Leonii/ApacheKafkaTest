import random
from datetime import datetime
from abc import ABC, abstractmethod

from simulation.content import data
from simulation.content.content import BaseContent, ApplicationLog, AccessLog, ServerMetrics

class IContentFactory(ABC):

    @abstractmethod
    def create_message_content(self, server_id: str) -> BaseContent:
        raise NotImplementedError()
    

class ApplicationLogFactory(IContentFactory):

    def create_message_content(self, server_id: str) -> BaseContent:
        return ApplicationLog(
            server_id = server_id,
            generation_time = datetime.now(),
            severity = random.choice(data.SEVERITY),
            msg = random.choice(data.MSGS),
            source_thread = random.choice(data.THREADS),
            source_cls = random.choice(data.CLSES)
        )
    
class AccessLogFactory(IContentFactory):

    def create_message_content(self, server_id: str) -> BaseContent:
        return AccessLog(
            server_id = server_id,
            generation_time = datetime.now(),
            request_method = random.choice(data.METHODS),
            user_ip = f"192.68.{random.randint(0,255)}.{random.randint(1,254)}",
            username = random.choice(data.USERS),
            response_status_code = random.choice(data.STATUS_CODES),
            response_dim = random.randint(500, 500_000),
            request_url = random.choice(data.URLS),
            user_agent = random.choice(data.USER_AGENTS)
        )
    
class ServerMetricsFactory(IContentFactory):

    def create_message_content(self, server_id: str) -> BaseContent:
        return ServerMetrics(
            server_id = server_id,
            generation_time = datetime.now(),
            cpu_usage = random.randint(30, 95),
            running_threads = random.randint(1, 30),
            current_users = random.randint(0,1500),
            open_files = random.randint(0,10)
        )