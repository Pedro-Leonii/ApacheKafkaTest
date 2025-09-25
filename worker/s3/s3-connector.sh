worker_addr=$1
s3_host=s3

topics=(servers.logs.access servers.logs.application servers.metrics)

for topic in ${topics[@]}; do 
    connector="s3-${topic//./-}"
    curl -i -X PUT -H "Accept:application/json"\
        -H "Content-Type:application/json" "http://$worker_addr:8083/connectors/$connector/config" \
        -d  @- <<EOF
{
    "connector.class": "io.confluent.connect.s3.S3SinkConnector",
    
    "tasks.max": 12,

    "topics": "$topic",
    "topics.dir": "topics",
    
    "rotate.interval.ms": 3600000,
    "flush.size": 1000,

    "auto.register.schemas": false,
    "use.latest.version": true,

    "store.url": "http://$s3_host:9095",
    "s3.bucket.name": "testbucket",
    "storage.class": "io.confluent.connect.s3.storage.S3Storage",
    "aws.access.key.id": "none",
    "aws.secret.access.key": "none",

    "partitioner.class": "io.confluent.connect.storage.partitioner.DailyPartitioner",
    "locale": "IT_it",
    "timezone": "Europe/Rome",
    "timestamp.extractor": "RecordField",
    "timestamp.field": "generation_time",

    "format.class": "io.confluent.connect.s3.format.parquet.ParquetFormat",
    "parquet.codec": "snappy"

}
EOF
done