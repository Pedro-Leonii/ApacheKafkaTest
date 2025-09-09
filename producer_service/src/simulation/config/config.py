BROKER_COMMON_CONFIG = {
    "bootstrap.servers":"broker1:9092,broker2:9092,broker3:9092",
    "acks":"all",
    "enable.idempotence": True,
    "linger.ms": 10,
    "batch.size": 1048576,
    "compression.type": "lz4",
    "partitioner": "murmur2_random"
}

NODE_ID = "node-1"

SCHEMA_REGISTRY_CONFIG = {
    "url":"http://schemaregistry:8085"
}