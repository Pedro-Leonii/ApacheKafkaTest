from abc import ABC, abstractmethod
from datetime import datetime 
from dataclasses import dataclass

@dataclass
class BaseContent(ABC):
    server_id: str
    generation_time: datetime

    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError()

@dataclass
class ApplicationLog(BaseContent):
    severity: str
    msg: str
    source_thread: str
    source_cls: str

    def to_dict(self):
        return dict(
            server_id=self.server_id,
            generation_time=self.generation_time,
            severity=self.severity,
            msg=self.msg,
            source_thread=self.source_thread,
            source_cls=self.source_cls
        )

@dataclass
class AccessLog(BaseContent):
    request_method: str
    user_ip: str
    username: str|None
    response_status_code: int
    request_url: str
    response_dim: int
    user_agent: str

    def to_dict(self):
        return dict(
            server_id=self.server_id,
            generation_time=self.generation_time,
            request_method=self.request_method,
            user_ip=self.user_ip,
            username=self.username,
            request_url=self.request_url,
            response_status_code=self.response_status_code,
            response_dim=self.response_dim,
            user_agent=self.user_agent
        )

@dataclass
class ServerMetrics(BaseContent):
    cpu_usage: int
    running_threads: int
    current_users: int
    open_files: int

    def to_dict(self):
        return dict(
            server_id=self.server_id,
            generation_time=self.generation_time,
            cpu_usage=self.cpu_usage,
            running_threads=self.running_threads,
            current_users=self.current_users,
            open_files=self.open_files
        )