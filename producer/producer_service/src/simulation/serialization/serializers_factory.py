from abc import ABC, abstractmethod
from importlib.resources import files

from simulation.serialization.serializers import ISerializer, AvroSerializer
from simulation.config.cfg import SCHEMA_REGISTRY_URL

class ISerializerFactory(ABC):

    @abstractmethod
    def create_app_log_serializer(self) -> ISerializer:
        pass

    @abstractmethod
    def create_metrics_serializer(self) -> ISerializer:
        pass

    @abstractmethod
    def create_access_log_serializer(self) -> ISerializer:
        pass

class AvroSerializerFactory(ISerializerFactory):

    def create_app_log_serializer(self) -> AvroSerializer:
        schema_str: str = files("simulation.serialization.avro").joinpath("app_log_schema.avsc").read_text()

        return AvroSerializer(
            schema_registry_url=SCHEMA_REGISTRY_URL,
            schema_str=schema_str
        )

    def create_metrics_serializer(self) -> AvroSerializer:
        schema_str: str = files("simulation.serialization.avro").joinpath("metrics_schema.avsc").read_text()

        return AvroSerializer(
            schema_registry_url=SCHEMA_REGISTRY_URL,
            schema_str=schema_str
        )
    
    def create_access_log_serializer(self) -> AvroSerializer:
        schema_str: str = files("simulation.serialization.avro").joinpath("access_log_schema.avsc").read_text()

        return AvroSerializer(
            schema_registry_url=SCHEMA_REGISTRY_URL,
            schema_str=schema_str
        )