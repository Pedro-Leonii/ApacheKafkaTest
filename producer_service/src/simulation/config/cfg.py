from os import environ

BOOTSTRAP_SERVERS = environ.get("BOOTSTRAP_SERVERS")
RESULTS_PATH = environ.get("RESULTS_PATH")
NODE_ID_LIST = environ.get("NODE_ID_LIST").split(",")
LAMBDA_LOGS = int(environ.get("LAMBDA_LOGS"))
INTERVAL_METRICS = int(environ.get("INTERVAL_METRICS"))
