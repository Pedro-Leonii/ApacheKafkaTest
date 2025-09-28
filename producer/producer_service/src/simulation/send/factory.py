from dataclasses import dataclass
from abc import ABC, abstractmethod
from importlib.resources import files

from simulation.content.factory import IContentFactory, ApplicationLogFactory, AccessLogFactory, ServerMetricsFactory
from simulation.serialization.serializers import IContentSerializer, ContentAvroSerializer
from simulation.send.request import SendRequest
from simulation.send import cfg

@dataclass
class ISendRequestFactory(ABC):

    content_factory: IContentFactory
    serializer: IContentSerializer

    @abstractmethod
    def generate_send_request(self) -> SendRequest:
        raise NotImplementedError()


class ApplicationLogSendRequestFactory(ISendRequestFactory):
    
    _TOPIC: str = "servers.logs.application"

    def __init__(self):

        schema: str = files("simulation.serialization.avro").joinpath("app_log_schema.avsc").read_text()

        serializer: ContentAvroSerializer = ContentAvroSerializer(
            schema_registry_url=cfg.SCHEMA_REGISTRY_URL,
            schema=schema,
            topic=ApplicationLogSendRequestFactory._TOPIC
        )

        content_factory: ApplicationLogFactory = ApplicationLogFactory()
        
        super().__init__(serializer=serializer, content_factory=content_factory) 

    def generate_send_request(self) -> SendRequest:

        return SendRequest(
            key=cfg.SERVER_ID,
            topic=self._TOPIC,
            content=self.serializer.serialize(self.content_factory.create_message_content(cfg.SERVER_ID))
        )

class AccessLogSendRequestFactory(ISendRequestFactory):
    
    _TOPIC: str = "servers.logs.access"

    def __init__(self):

        schema: str = files("simulation.serialization.avro").joinpath("access_log_schema.avsc").read_text()

        serializer: ContentAvroSerializer = ContentAvroSerializer(
            schema_registry_url=cfg.SCHEMA_REGISTRY_URL,
            schema=schema,
            topic=AccessLogSendRequestFactory._TOPIC
        )

        content_factory: AccessLogFactory = AccessLogFactory()
        
        super().__init__(serializer=serializer, content_factory=content_factory) 

    def generate_send_request(self) -> SendRequest:

        return SendRequest(
            key=cfg.SERVER_ID,
            topic=self._TOPIC,
            content=self.serializer.serialize(self.content_factory.create_message_content(cfg.SERVER_ID))
        )
    
class ServerMetricsRequestFactory(ISendRequestFactory):
    
    _TOPIC: str = "servers.metrics"

    def __init__(self):

        schema: str = files("simulation.serialization.avro").joinpath("server_metrics_schema.avsc").read_text()

        serializer: ContentAvroSerializer = ContentAvroSerializer(
            schema_registry_url=cfg.SCHEMA_REGISTRY_URL,
            schema=schema,
            topic=ServerMetricsRequestFactory._TOPIC
        )

        content_factory: ServerMetricsFactory = ServerMetricsFactory()
        
        super().__init__(serializer=serializer, content_factory=content_factory) 

    def generate_send_request(self) -> SendRequest:

        return SendRequest(
            key=cfg.SERVER_ID,
            topic=ServerMetricsRequestFactory._TOPIC,
            content=self.serializer.serialize(self.content_factory.create_message_content(cfg.SERVER_ID))
        )