curl -i -X PUT -H "Accept:application/json"\
    -H "Content-Type:application/json" http://localhost:8083/connectors/sink-s3-access-log/config \
    -d '
    {
        "connector.class": "io.confluent.connect.s3.S3SinkConnector",
        
        "task.max": "1",

        "topics": "server.logs.access",
        "topics.dir": "topics",
        
        "rotate.interval.ms": "3600000",
        "flush.size": 1000,

        "store.kafka.keys": "true",

        "auto.register.schemas": "false",
        "use.latest.version": "true",

        "store.url": "http://s3proxy:8080",
        "s3.bucket.name": "testbucket",
        "storage.class": "io.confluent.connect.s3.storage.S3Storage",
        "aws.access.key.id": "none",
        "aws.secret.access.key": "none",

        "partitioner.class": "io.confluent.connect.storage.partitioner.DailyPartitioner",
        "locale": "it_IT",
        "timestamp.extractor": "RecordField",
        "timestamp.field": "datetime",
        "timezone": "UTC",

        "format.class": "io.confluent.connect.s3.format.parquet.ParquetFormat",
        "parquet.codec": "snappy",

        "errors.tolerance": "all",
        "errors.log.enable": "true",
        "errors.deadletterqueue.topic.name": "dlq-topic"
    

    }
'

curl -i -X PUT -H "Accept:application/json"\
    -H "Content-Type:application/json" http://localhost:8083/connectors/sink-s3-app-log/config \
    -d '
    {
        "connector.class": "io.confluent.connect.s3.S3SinkConnector",
        
        "task.max": "1",

        "topics": "server.logs.application",
        "topics.dir": "topics",
        
        "rotate.interval.ms": "3600000",
        "flush.size": 1000,

        "store.kafka.keys": "true",

        "auto.register.schemas": "false",
        "use.latest.version": "true",

        "store.url": "http://s3proxy:8080",
        "s3.bucket.name": "testbucket",
        "storage.class": "io.confluent.connect.s3.storage.S3Storage",
        "aws.access.key.id": "none",
        "aws.secret.access.key": "none",

        "partitioner.class": "io.confluent.connect.storage.partitioner.DailyPartitioner",
        "locale": "it_IT",
        "timestamp.extractor": "RecordField",
        "timestamp.field": "datetime",
        "timezone": "UTC",

        "format.class": "io.confluent.connect.s3.format.parquet.ParquetFormat",
        "parquet.codec": "snappy",

        "errors.tolerance": "all",
        "errors.log.enable": "true",
        "errors.deadletterqueue.topic.name": "dlq-topic"
    

    }
'

curl -i -X PUT -H "Accept:application/json"\
    -H "Content-Type:application/json" http://localhost:8083/connectors/sink-s3-metrics/config \
    -d '
    {
        "connector.class": "io.confluent.connect.s3.S3SinkConnector",
        
        "task.max": "1",

        "topics": "server.metrics",
        "topics.dir": "topics",
        
        "rotate.interval.ms": "3600000",
        "flush.size": 1000,

        "store.kafka.keys": "true",

        "auto.register.schemas": "false",
        "use.latest.version": "true",

        "store.url": "http://s3proxy:8080",
        "s3.bucket.name": "testbucket",
        "storage.class": "io.confluent.connect.s3.storage.S3Storage",
        "aws.access.key.id": "none",
        "aws.secret.access.key": "none",

        "partitioner.class": "io.confluent.connect.storage.partitioner.DailyPartitioner",
        "locale": "it_IT",
        "timestamp.extractor": "RecordField",
        "timestamp.field": "datetime",
        "timezone": "UTC",

        "format.class": "io.confluent.connect.s3.format.parquet.ParquetFormat",
        "parquet.codec": "snappy",

        "errors.tolerance": "all",
        "errors.log.enable": "true",
        "errors.deadletterqueue.topic.name": "dlq-topic"
    

    }
'