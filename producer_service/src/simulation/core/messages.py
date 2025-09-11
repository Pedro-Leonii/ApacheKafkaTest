from abc import ABC

from dataclasses import dataclass
from datetime import datetime 

@dataclass
class BaseMessage(ABC):

    source: str
    datetime: datetime

@dataclass
class ApplicationLogMessage(BaseMessage):
    severity: str
    msg: str
    thread: str
    cls: str

@dataclass
class AccessLogMessage(BaseMessage):
    method: str
    ip: str
    user: str|None
    status_code: int
    url: str
    dim: int
    user_agent: str

@dataclass
class ServerMetricsMessage(BaseMessage):
    cpu: int
    threads: int
    users: int
    open_files: int