import json
import uuid
from threading import Event

from confluent_kafka import Producer

from simulation.runner.runners import MetricsRunner, LogRunner
from simulation.serialization.serializers_factory import AvroSerializerFactory
from simulation.sender.senders_factory import SenderFactory
from simulation.config.cfg import INTERVAL_METRICS, BOOTSTRAP_SERVERS, LAMBDA_LOGS

class ServerSimulation:

    COMMON_CONFIG: dict = {
        "bootstrap.servers": BOOTSTRAP_SERVERS,
        "acks":"all",
        "enable.idempotence": True,
        "linger.ms": 200,
        "batch.size": 1048576,
        "compression.type": "lz4",
        "partitioner": "murmur2_random"
    }

    def generate_server_id() -> str:
        return f"node-{uuid.uuid4()}"

    def __init__(self):
        
        self._server_id = ServerSimulation.generate_server_id()

        self._stop_event = Event()
        self._kafka_producer = Producer({
            **ServerSimulation.COMMON_CONFIG,
            "client.id": self._server_id
        }) 
        
        avro_serializer_factory = AvroSerializerFactory()

        metrics_sender=SenderFactory.create_metrics_sender(
            server_id=self._server_id,
            serializer_factory=avro_serializer_factory,
            kafka_producer=self._kafka_producer
        )
        
        self._metrics_runner = MetricsRunner(
            stop_event=self._stop_event,
            t=INTERVAL_METRICS,
            metrics_sender=metrics_sender
            
        )

        access_log_sender=SenderFactory.create_access_log_sender(
            server_id=self._server_id,
            serializer_factory=avro_serializer_factory,
            kafka_producer=self._kafka_producer
        )
        application_log_sender=SenderFactory.create_app_log_sender(
            server_id=self._server_id,
            serializer_factory=avro_serializer_factory,
            kafka_producer=self._kafka_producer
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
        self._kafka_producer.flush()
