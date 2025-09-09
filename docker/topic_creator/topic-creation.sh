#!/bin/bash

topics="server.metrics server.logs.application server.logs.access"
bootstrap_servers="broker1:9092, broker2:9092, broker3:9092"
partitions=1
replication_factor=3
min_insync_replicas=2

for topic in $topics; do
    /opt/kafka/bin/kafka-topics.sh --create \
        --topic "$topic" \
        --if-not-exists \
        --partitions $partitions \
        --replication-factor $replication_factor \
        --config min.insync.replicas=$min_insync_replicas \
        --bootstrap-server $bootstrap_servers
done


