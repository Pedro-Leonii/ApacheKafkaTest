from abc import abstractmethod, ABC
from enum import Enum
from datetime import datetime


class ISendable(ABC):
    
    @abstractmethod
    def to_dict(self) -> dict:
        ...
    

class Severity(Enum):
    SEVERE = "SEVERE"
    FINE = "FINE"
    WARNING = "WARNING"
    INFO = "INFO"

class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"
    CONNECT = "CONNECT"
    OPTIONS = "OPTIONS"
    TRACE = "TRACE"
    PATCH = "PATCH"

class AppLog(ISendable):

    def __init__(
            self, datetime: datetime, severity: Severity, 
            msg: str, thread: str, cls: str):
        
        self._datetime = datetime
        self._severity = severity
        self._msg = msg
        self._thread = thread
        self._cls = cls

    @property
    def datetime(self) -> datetime:
        return self._datetime
    
    @property
    def severity(self) -> Severity:
        return self._severity
    
    @property
    def msg(self) -> str:
        return self._msg
    
    @property
    def thread(self) -> str:
        return self._thread
    
    @property
    def cls(self) -> str:
        return self._cls
    
    def to_dict(self)->dict:
        return dict(    
            datetime = self._datetime.timestamp()*1000,
            severity = self._severity.name,
            msg = self._msg,
            thread = self._thread,
            cls = self._cls,
        )

class AccessLog(ISendable):

    def __init__(self, ip: str, user: str|None, status_code: int, dim: int, url: str, uagent: str, method: HttpMethod, datetime: datetime):
        self._datetime = datetime
        self._ip = ip
        self._user = user
        self._status_code = status_code
        self._dim = dim
        self._url = url
        self._uagent = uagent
        self._method = method

    @property
    def ip(self) -> str:
        return self._ip
    
    @property
    def user(self) -> str|None:
        return self._user

    @property
    def status_code(self) -> int:
        return self._status_code
    
    @property
    def dim(self) -> int:
        return self._dim
    
    @property
    def url(self) -> str:
        return self._url
    
    @property
    def uagent(self) -> str:
        return self._uagent
    
    @property
    def method(self) -> str:
        return self._method
    
    @property
    def datetime(self) -> datetime:
        return self._datetime
    
    def to_dict(self)->dict:
        return dict(    
            datetime = self._datetime.timestamp()*1000,
            ip = self._ip,
            user = self._user,
            status_code = self._status_code,
            dim = self._dim,
            url = self._url,
            user_agent = self._uagent,
            method = self._method.name
        )

class Metrics(ISendable):

    def __init__(self, cpu: int, threads: int, users: int, datetime: datetime, open_files: int):

        self._cpu = cpu
        self._threads = threads
        self._users = users
        self._datetime = datetime
        self._open_files = open_files
    
    @property
    def cpu(self) -> int:
        return self._cpu
    
    @property
    def threads(self) -> int:
        return self._threads
    
    @property
    def users(self) -> int:
        return self._users
    
    @property
    def open_files(self) -> int:
        return self._open_files

    @property
    def datetime(self) -> datetime:
        return self._datetime
    
    def to_dict(self)->dict:
        return dict(   
            datetime = self._datetime.timestamp()*1000, 
            cpu = self._cpu,
            threads = self._threads,
            users = self._users,
            open_files = self._open_files,
        )