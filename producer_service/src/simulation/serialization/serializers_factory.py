from abc import ABC, abstractmethod
from importlib.resources import files

from simulation.serialization.serializers import ISerializer, AvroSerializer

class ISerializerFactory(ABC):

    SCHEMA_REGISTRY_URL: str = "http://schemaregistry:8085"

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
        schema_str: str = files("simulation.serialization.schemas").joinpath("app_log_schema.avsc").read_text()

        return AvroSerializer(
            schema_registry_url=ISerializerFactory.SCHEMA_REGISTRY_URL,
            schema_str=schema_str
        )

    def create_metrics_serializer(self) -> AvroSerializer:
        schema_str: str = files("simulation.serialization.schemas").joinpath("metrics_schema.avsc").read_text()

        return AvroSerializer(
            schema_registry_url=ISerializerFactory.SCHEMA_REGISTRY_URL,
            schema_str=schema_str
        )
    
    def create_access_log_serializer(self) -> AvroSerializer:
        schema_str: str = files("simulation.serialization.schemas").joinpath("access_log_schema.avsc").read_text()

        return AvroSerializer(
            schema_registry_url=ISerializerFactory.SCHEMA_REGISTRY_URL,
            schema_str=schema_str
        )