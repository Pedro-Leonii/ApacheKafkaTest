#!/bin/bash

TOPICS=(servers.metrics servers.logs.application servers.logs.access)
SERVERS=$1
INSYNC=2
REPLICATION=3
PARTITION=12


for TOPIC in ${TOPICS[@]}; do
        kafka-topics.sh --create \
        --topic $TOPIC \
        --if-not-exists \
        --partitions $PARTITION \
        --replication-factor $REPLICATION \
        --config min.insync.replicas=$INSYNC \
        --bootstrap-server $SERVERS
done


kafka-topics.sh --create \
        --topic _schemas \
        --if-not-exists \
        --partitions 1 \
        --replication-factor $REPLICATION \
        --config min.insync.replicas=$INSYNC \
        --config cleanup.policy=compact \
        --bootstrap-server $SERVERS
