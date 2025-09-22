WORKER_ADDR=$1
S3_URL=$2

CONNECTOR="s3-sink-connector"
TOPICS="servers.logs.access, servers.logs.application, servers.metrics"

curl -i -X PUT -H "Accept:application/json"\
        -H "Content-Type:application/json" http://$WORKER_ADDR/connectors/$CONNECTOR/config \
        -d  @- <<EOF
        {
            "connector.class": "io.confluent.connect.s3.S3SinkConnector",
            
            "tasks.max": 36,

            "topics": "$TOPICS",
            "topics.dir": "topics",
            
            "rotate.interval.ms": 3600000,
            "flush.size": 1000,

            "auto.register.schemas": false,
            "use.latest.version": true,

            "store.url": "$S3_URL",
            "s3.bucket.name": "testbucket",
            "storage.class": "io.confluent.connect.s3.storage.S3Storage",
            "aws.access.key.id": "none",
            "aws.secret.access.key": "none",

            "partitioner.class": "io.confluent.connect.storage.partitioner.DailyPartitioner",
            "locale": "it_IT",
            "timestamp.extractor": "RecordField",
            "timestamp.field": "generation_time",
            "timezone": "UTC",

            "format.class": "io.confluent.connect.s3.format.parquet.ParquetFormat",
            "parquet.codec": "snappy"

        }
    
