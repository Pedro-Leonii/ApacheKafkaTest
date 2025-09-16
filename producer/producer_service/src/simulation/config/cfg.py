from os import environ

BOOTSTRAP_SERVERS = environ.get("BOOTSTRAP_SERVERS")
RESULTS_PATH = environ.get("RESULTS_CONTAINER_PATH")
NODES_NUM = int(environ.get("NODES_NUM"))
LAMBDA_LOGS = int(environ.get("LAMBDA_LOGS"))
INTERVAL_METRICS = int(environ.get("INTERVAL_METRICS"))
SCHEMA_REGISTRY_URL = environ.get("SCHEMA_REGISTRY_URL")
