import json

from confluent_kafka import Producer

from simulation.sender.sender import Sender
from simulation.serialization.serializers_factory import ISerializerFactory
from simulation.generation.generators import ServerMetricsRandomGeneration, ApplicationLogRandomGeneration, AccessLogRandomGeneration
from simulation.result.writer import writer
from simulation.config.cfg import BOOTSTRAP_SERVERS

def stats_cb(stats: str):
    writer.write(json.loads(stats))

class SenderFactory:

    _PRODUCER: Producer = Producer({
        "bootstrap.servers": BOOTSTRAP_SERVERS,
        "acks":"all",
        "enable.idempotence": True,
        "linger.ms": 500,
        "batch.size": 1048576,
        "compression.type": "lz4",
        "partitioner": "murmur2_random",
        "stats_cb": stats_cb,
        "statistics.interval.ms": 1000
    })

    def create_app_log_sender(source:str, serializer_factory: ISerializerFactory) -> Sender:
        return Sender(
            msg_factory=ApplicationLogRandomGeneration(),
            k_producer=SenderFactory._PRODUCER,
            serializer=serializer_factory.create_app_log_serializer(),
            source=source,
            topic="server.logs.application"
        )
    
    def create_access_log_sender(source: str, serializer_factory: ISerializerFactory) -> Sender:
        return Sender(
            msg_factory=AccessLogRandomGeneration(),
            k_producer=SenderFactory._PRODUCER,
            serializer=serializer_factory.create_access_log_serializer(),
            source=source,
            topic="server.logs.access"
        )
    
    def create_metrics_sender(source: str, serializer_factory: ISerializerFactory) -> Sender:
        return Sender(
            msg_factory=ServerMetricsRandomGeneration(),
            k_producer=SenderFactory._PRODUCER,
            serializer=serializer_factory.create_metrics_serializer(),
            source=source,
            topic="server.metrics"
        )