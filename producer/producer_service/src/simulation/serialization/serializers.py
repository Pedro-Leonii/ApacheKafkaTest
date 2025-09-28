from abc import ABC, abstractmethod

from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient

from simulation.content.content import BaseContent

class IContentSerializer(ABC):

    @abstractmethod
    def serialize(self, message: BaseContent) -> bytes:
        raise NotImplementedError()

class ContentAvroSerializer(IContentSerializer):

    def __init__(self, schema_registry_url: str, schema: str, topic: str):

        self._context = SerializationContext(topic=topic, field=MessageField.VALUE) 

        client: SchemaRegistryClient = SchemaRegistryClient({"url":schema_registry_url})

        self._serializer = AvroSerializer(
            schema_registry_client=client, 
            schema_str=schema
        )

    def serialize(self, message: BaseContent) -> bytes:
        return self._serializer(message.to_dict(), self._context)