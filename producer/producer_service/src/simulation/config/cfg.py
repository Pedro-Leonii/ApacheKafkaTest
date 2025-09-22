from os import environ

BOOTSTRAP_SERVERS = environ.get("BOOTSTRAP_SERVERS")
LAMBDA_LOGS = float(environ.get("LAMBDA_LOGS"))
INTERVAL_METRICS = float(environ.get("INTERVAL_METRICS"))
SCHEMA_REGISTRY_URL = environ.get("SCHEMA_REGISTRY_URL")
