from abc import ABC, abstractmethod

from confluent_kafka import Producer

from simulation.sender.sender import Sender
from simulation.serialization.serializers_factory import ISerializerFactory
from simulation.generation.generators import ServerMetricsRandomGeneration, ApplicationLogRandomGeneration, AccessLogRandomGeneration

class SenderFactory:

    _PRODUCER: Producer = Producer({
        "bootstrap.servers":"broker1:9092,broker2:9092,broker3:9092",
        "acks":"all",
        "enable.idempotence": True,
        "linger.ms": 500,
        "batch.size": 1048576,
        "compression.type": "lz4",
        "partitioner": "murmur2_random"
    })

    def create_app_log_producer(source:str, serializer_factory: ISerializerFactory) -> Sender:
        return Sender(
            msg_factory=ApplicationLogRandomGeneration(),
            k_producer=SenderFactory._PRODUCER,
            serializer=serializer_factory.create_app_log_serializer(),
            source=source,
            topic="server.logs.application"
        )
    
    def create_access_log_producer(source: str, serializer_factory: ISerializerFactory) -> Sender:
        return Sender(
            msg_factory=AccessLogRandomGeneration(),
            k_producer=SenderFactory._PRODUCER,
            serializer=serializer_factory.create_access_log_serializer(),
            source=source,
            topic="server.logs.access"
        )
    
    def create_metrics_producer(source: str, serializer_factory: ISerializerFactory) -> Sender:
        return Sender(
            msg_factory=ServerMetricsRandomGeneration(),
            k_producer=SenderFactory._PRODUCER,
            serializer=serializer_factory.create_metrics_serializer(),
            source=source,
            topic="server.metrics"
        )