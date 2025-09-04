import os

from confluent_kafka import Producer as KProducer

from simulation.producers.producers import Producer
from simulation.messages.serialization import JsonSerializerVisitor
from simulation.messages.factories import AppLogFactory, AccessLogFactory, MetricsFactory
from simulation.messages.generation import AccessLogRandomGeneration, ApplicationLogRandomGeneration, MetricsRandomGeneration

class ProducerFactory:

    NODE: str = "node1"

    def create_application_log_producer() -> Producer:
        return Producer(
            sendable_factory=AppLogFactory(ApplicationLogRandomGeneration()),
            k_producer=KProducer(get_kproducer_common_config()),
            topic='server.logs.application',
            node_id=ProducerFactory.NODE,     
            serializer=JsonSerializerVisitor()
        )
        
    def create_access_log_producer() -> Producer:
        return Producer(
            sendable_factory=AccessLogFactory(AccessLogRandomGeneration()),
            k_producer=KProducer(get_kproducer_common_config()),
            topic='server.logs.access',
            node_id=ProducerFactory.NODE,     
            serializer=JsonSerializerVisitor()
        )
        
    def create_metrics_producer() -> Producer:
        return Producer(
            sendable_factory=MetricsFactory(MetricsRandomGeneration()),
            k_producer=KProducer(get_kproducer_common_config()),
            topic='server.metrics',
            node_id=ProducerFactory.NODE,     
            serializer=JsonSerializerVisitor()
        )
    

def get_kproducer_common_config() -> dict:
    return {
            "bootstrap.servers": os.environ['BOOTSTRAP_SERVERS'],
            "acks": os.environ['ACKS']
        }