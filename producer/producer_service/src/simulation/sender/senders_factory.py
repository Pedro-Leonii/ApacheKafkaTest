from confluent_kafka import Producer

from simulation.sender.sender import Sender
from simulation.serialization.serializers_factory import ISerializerFactory
from simulation.generation.generators import ServerMetricsRandomGeneration, ApplicationLogRandomGeneration, AccessLogRandomGeneration

class SenderFactory:

    def create_app_log_sender(source:str, serializer_factory: ISerializerFactory, kafka_producer: Producer) -> Sender:
        return Sender(
            msg_factory=ApplicationLogRandomGeneration(),
            k_producer=kafka_producer,
            serializer=serializer_factory.create_app_log_serializer(),
            source=source,
            topic="server.logs.application"
        )
    
    def create_access_log_sender(source: str, serializer_factory: ISerializerFactory, kafka_producer: Producer) -> Sender:
        return Sender(
            msg_factory=AccessLogRandomGeneration(),
            k_producer=kafka_producer,
            serializer=serializer_factory.create_access_log_serializer(),
            source=source,
            topic="server.logs.access"
        )
    
    def create_metrics_sender(source: str, serializer_factory: ISerializerFactory, kafka_producer: Producer) -> Sender:
        return Sender(
            msg_factory=ServerMetricsRandomGeneration(),
            k_producer=kafka_producer,
            serializer=serializer_factory.create_metrics_serializer(),
            source=source,
            topic="server.metrics"
        )