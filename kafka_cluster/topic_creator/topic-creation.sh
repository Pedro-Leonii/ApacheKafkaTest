#!/bin/bash

servers="broker1:10001,broker2:10002,broker3:10003"
insync=2
replication=3
partition_n=12
topics=(servers.metrics servers.logs.application servers.logs.access)

until /opt/kafka/bin/kafka-topics.sh --bootstrap-server $servers --list; do
  echo "Waiting for Kafka brokers..."
  sleep 1
done


for topic in ${topics[@]}; do
        /opt/kafka/bin/kafka-topics.sh --create \
        --topic $topic \
        --if-not-exists \
        --partitions $partition_n \
        --replication-factor $replication \
        --config min.insync.replicas=$insync \
        --bootstrap-server $servers
done


/opt/kafka/bin/kafka-topics.sh --create \
        --topic _schemas \
        --if-not-exists \
        --partitions 1 \
        --replication-factor $replication \
        --config min.insync.replicas=$insync \
        --config cleanup.policy=compact \
        --bootstrap-server $servers
