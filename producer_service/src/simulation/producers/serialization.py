from abc import ABC, abstractmethod
from pathlib import Path

from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient

from simulation.messages.content import ISendable

class ISerializer(ABC):

    @abstractmethod
    def serialize(self, value: ISendable, topic:str):
        ...


class AvroSerializerAdapter(ISerializer):

    def __init__(self, client: SchemaRegistryClient, schema_path: Path):
        
        schema_str: str =""

        with open(schema_path, "r") as schema:
            schema_str = schema.read()

        self._serializer = AvroSerializer(
            schema_registry_client=client,
            schema_str=schema_str
        )

    def serialize(self, value: ISendable, topic:str):
        return self._serializer(value.to_dict(), SerializationContext(topic,MessageField.VALUE))
        