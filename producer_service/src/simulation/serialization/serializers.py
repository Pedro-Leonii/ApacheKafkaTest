from abc import ABC, abstractmethod
from dataclasses import asdict

from confluent_kafka.schema_registry.avro import AvroSerializer as KAvroSerializer
from confluent_kafka.serialization import SerializationContext
from confluent_kafka.schema_registry import SchemaRegistryClient

from simulation.core.messages import BaseMessage

class ISerializer(ABC):

    @abstractmethod
    def serialize(self, message: BaseMessage, context: SerializationContext):
        ...


class AvroSerializer(ISerializer):

    def __init__(self, schema_registry_url: str, schema_str: str):
        client: SchemaRegistryClient = SchemaRegistryClient({"url":schema_registry_url})
        self._serializer = KAvroSerializer(
            schema_registry_client=client, 
            schema_str=schema_str
        )

    def serialize(self, message: dict, context: SerializationContext):
        return self._serializer(message, context)
