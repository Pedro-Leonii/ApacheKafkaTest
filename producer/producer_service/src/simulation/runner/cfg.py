from os import environ

LAMBDA_LOGS = float(environ.get("LAMBDA_LOGS"))
INTERVAL_METRICS = float(environ.get("INTERVAL_METRICS"))

