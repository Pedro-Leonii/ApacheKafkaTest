#!/bin/bash

topics="server.metrics server.logs.application server.logs.access"
bootstrap_servers="broker1:9092, broker2:9092, broker3:9092"
partitions=12
replication_factor=3
min_insync_replicas=2


/opt/kafka/bin/kafka-topics.sh --create \
        --topic _schemas \
        --if-not-exists \
        --partitions 1 \
        --replication-factor 3 \
        --config min.insync.replicas=3, cleanup.policy=compact \
        --bootstrap-server $bootstrap_servers

for topic in $topics; do
    /opt/kafka/bin/kafka-topics.sh --create \
        --topic "$topic" \
        --if-not-exists \
        --partitions $partitions \
        --replication-factor $replication_factor \
        --config min.insync.replicas=$min_insync_replicas \
        --bootstrap-server $bootstrap_servers
done