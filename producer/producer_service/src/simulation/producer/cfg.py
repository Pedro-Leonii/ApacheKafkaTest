from os import environ

PRODUCER_CONFIG = {
    "bootstrap.servers": environ.get("BOOTSTRAP_SERVERS"),
    "acks":"all",
    "enable.idempotence": True,
    "linger.ms": 500,
    "batch.size": 1048576,
    "compression.type": "lz4",
    "partitioner": "murmur2_random"
}