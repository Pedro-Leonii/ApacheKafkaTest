import os
from pathlib import Path

from confluent_kafka import Producer as KProducer
from confluent_kafka.schema_registry import SchemaRegistryClient

from simulation.producers.producers import Producer
from simulation.messages.creation import AppLogFactory, AccessLogFactory, MetricsFactory
from simulation.messages.generation import AccessLogRandomGeneration, ApplicationLogRandomGeneration, MetricsRandomGeneration
from simulation.config.config import BROKER_COMMON_CONFIG, NODE_ID, SCHEMA_REGISTRY_CONFIG
from simulation.producers.serialization import AvroSerializerAdapter


class ProducerFactory:

    def create_application_log_producer() -> Producer:

        return Producer(
            sendable_factory=AppLogFactory(ApplicationLogRandomGeneration()),
            k_producer=KProducer(BROKER_COMMON_CONFIG),
            topic="server.logs.application",
            node_id=NODE_ID,
            serializer=AvroSerializerAdapter(
                SchemaRegistryClient(SCHEMA_REGISTRY_CONFIG),
                Path(__file__).parent / "schemas/app_log_schema.avsc"
            ) 
        )
        

    def create_access_log_producer() -> Producer:
        return Producer(
            sendable_factory=AccessLogFactory(AccessLogRandomGeneration()),
            k_producer=KProducer(BROKER_COMMON_CONFIG),
            topic="server.logs.access",
            node_id=NODE_ID,     
            serializer=AvroSerializerAdapter(
                SchemaRegistryClient(SCHEMA_REGISTRY_CONFIG),
                Path(__file__).parent / "schemas/access_log_schema.avsc"
            ) 
        )
        
    def create_metrics_producer() -> Producer:
        
        return Producer(
            sendable_factory=MetricsFactory(MetricsRandomGeneration()),
            k_producer=KProducer(BROKER_COMMON_CONFIG),
            topic="server.metrics",
            node_id=NODE_ID,     
            serializer= AvroSerializerAdapter(
                SchemaRegistryClient(SCHEMA_REGISTRY_CONFIG),
                Path(__file__).parent / "schemas/metrics_schema.avsc"
            )
        )
    
    