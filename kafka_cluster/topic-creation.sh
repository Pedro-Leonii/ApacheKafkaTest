#!/bin/bash

servers="broker1:9092, broker2:9093, broker3:9094"
insync=2
replication=3
partition_n=12
topics=(servers.metrics servers.logs.application servers.logs.access)


for topic in ${topics[@]}; do
        kafka-topics.sh --create \
        --topic $topic \
        --if-not-exists \
        --partitions $partition_n \
        --replication-factor $replication \
        --config min.insync.replicas=$insync \
        --bootstrap-server $servers
done


kafka-topics.sh --create \
        --topic _schemas \
        --if-not-exists \
        --partitions 1 \
        --replication-factor $replication \
        --config min.insync.replicas=$insync \
        --config cleanup.policy=compact \
        --bootstrap-server $servers
