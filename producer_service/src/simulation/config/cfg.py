from os import environ

BOOTSTRAP_SERVERS = environ.get("BOOTSTRAP_SERVERS")
NODE_ID = environ.get("NODE_ID")
LAMBDA_LOGS = environ.get("LAMBDA_LOGS")
INTERVAL_METRICS = environ.get("INTERVAL_METRICS")
