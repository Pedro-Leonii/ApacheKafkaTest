/opt/kafka/bin/kafka-topics.sh --create \
        --topic _schemas \
        --if-not-exists \
        --partitions 1 \
        --replication-factor 3 \
        --config min.insync.replicas=3 \
        --config cleanup.policy=compact \
        --bootstrap-server broker1:9092, broker2:9092, broker3:9092

/opt/kafka/bin/kafka-topics.sh --create \
        --topic server.metrics \
        --if-not-exists \
        --partitions 12 \
        --replication-factor 3 \
        --config min.insync.replicas=2 \
        --bootstrap-server broker1:9092, broker2:9092, broker3:9092

/opt/kafka/bin/kafka-topics.sh --create \
        --topic server.logs.application \
        --if-not-exists \
        --partitions 12 \
        --replication-factor 3 \
        --config min.insync.replicas=2 \
        --bootstrap-server broker1:9092, broker2:9092, broker3:9092

/opt/kafka/bin/kafka-topics.sh --create \
        --topic server.logs.access \
        --if-not-exists \
        --partitions 12 \
        --replication-factor 3 \
        --config min.insync.replicas=2 \
        --bootstrap-server broker1:9092, broker2:9092, broker3:9092