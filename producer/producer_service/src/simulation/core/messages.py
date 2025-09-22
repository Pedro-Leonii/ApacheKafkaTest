from abc import ABC
from datetime import datetime 
from dataclasses import dataclass

@dataclass
class BaseMessage(ABC):

    server_id: str
    generation_time: datetime

@dataclass
class ApplicationLogMessage(BaseMessage):
    severity: str
    msg: str
    source_thread: str
    source_cls: str

@dataclass
class AccessLogMessage(BaseMessage):
    request_method: str
    user_ip: str
    username: str|None
    response_status_code: int
    request_url: str
    response_dim: int
    user_agent: str

@dataclass
class ServerMetricsMessage(BaseMessage):
    cpu_usage: int
    running_threads: int
    current_users: int
    open_files: int