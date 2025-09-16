import json
import uuid
from threading import Event

from confluent_kafka import Producer

from simulation.runner.runners import MetricsRunner, LogRunner
from simulation.serialization.serializers_factory import AvroSerializerFactory
from simulation.sender.senders_factory import SenderFactory
from simulation.config.cfg import INTERVAL_METRICS, BOOTSTRAP_SERVERS, LAMBDA_LOGS
from simulation.result.writer import writer

def stats_cb(stats: str):
    writer.write(json.loads(stats))

class NodeSimulation:

    COMMON_CONFIG: dict = {
        "bootstrap.servers": BOOTSTRAP_SERVERS,
        "acks":"all",
        "enable.idempotence": True,
        "linger.ms": 200,
        "batch.size": 1048576,
        "compression.type": "lz4",
        "partitioner": "murmur2_random",
        "statistics.interval.ms": 5000,
        "stats_cb": stats_cb
    }

    def generate_node_id() -> str:
        return f"node-{uuid.uuid4()}"

    def __init__(self):

        node_id: str = NodeSimulation.generate_node_id()

        self._stop_event = Event()
        kafka_producer = Producer({
            **NodeSimulation.COMMON_CONFIG,
            "client.id": node_id
        }) 
        
        avro_serializer_factory = AvroSerializerFactory()

        metrics_sender=SenderFactory.create_metrics_sender(
            source=node_id,
            serializer_factory=avro_serializer_factory,
            kafka_producer=kafka_producer
        )
        self._metrics_runner = MetricsRunner(
            stop_event=self._stop_event,
            t=INTERVAL_METRICS,
            metrics_sender=metrics_sender
            
        )

        access_log_sender=SenderFactory.create_access_log_sender(
            source=node_id,
            serializer_factory=avro_serializer_factory,
            kafka_producer=kafka_producer
        )
        application_log_sender=SenderFactory.create_app_log_sender(
            source=node_id,
            serializer_factory=avro_serializer_factory,
            kafka_producer=kafka_producer
        )
        self._log_runner = LogRunner(
            stop_event=self._stop_event,
            l=LAMBDA_LOGS,
            application_log_sender=application_log_sender,
            access_log_sender=access_log_sender
        )
    
    def start(self) -> None:
        self._log_runner.start()
        self._metrics_runner.start()
    
    def stop(self) -> None:
        self._stop_event.set()
        self._log_runner.join()
        self._metrics_runner.join()
