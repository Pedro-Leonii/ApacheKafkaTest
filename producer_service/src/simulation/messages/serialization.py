from abc import ABC, abstractmethod
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from simulation.messages.records import AccessLog, AppLog, Metrics

class ISerializerVisitor(ABC):

    @abstractmethod
    def serialize_access_log(self, log: "AccessLog") -> str|bytes:
        ...

    @abstractmethod
    def serialize_application_log(self, log: "AppLog") -> str|bytes:
        ...

    @abstractmethod
    def serialize_metrics(self, metrics: "Metrics") -> str|bytes:
        ...

class JsonSerializerVisitor(ISerializerVisitor):

    def serialize_application_log(self, log: "AppLog") -> str|bytes:
        data: dict = {
            "datetime": str(log.datetime), 
            "severity": str(log.severity),
            "message": log.msg,
            "thread": log.thread,
            "class": log.cls
        }
        return json.dumps(data)

    def serialize_access_log(self, log: "AccessLog") -> str|bytes:
        data: dict = {
            "datetime": str(log.datetime), 
            "ip": log.ip,
            "user": log.user,
            "status": log.status_code,
            "dim": log.dim,
            "url": log.url,
            "method": log.method,
            "user_agent": log.uagent
        }
        return json.dumps(data)
    
    def serialize_metrics(self, metrics: "Metrics") -> str|bytes:
        data: dict = {
            "datetime": str(metrics.datetime), 
            "cpu": metrics.cpu,
            "users": metrics.users,
            "open_files": metrics.open_files,
            "threads": metrics.threads
        }
        return json.dumps(data)
