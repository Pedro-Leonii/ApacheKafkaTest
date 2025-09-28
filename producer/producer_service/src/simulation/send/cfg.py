from os import environ
from uuid import uuid4

SCHEMA_REGISTRY_URL = environ.get("SCHEMA_REGISTRY_URL")
SERVER_ID: str = f"node-{uuid4()}"