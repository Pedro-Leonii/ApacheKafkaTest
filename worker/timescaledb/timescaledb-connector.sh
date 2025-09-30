worker_addr=$1
connection_password=$2
connection_url="jdbc:postgresql://timescaledb:10010/kafka"
connection_user="postgres"

topics=(servers.logs.access servers.logs.application servers.metrics)

for topic in ${topics[@]}; do 
    connector="timescaledb-${topic//./-}"
    curl -i -X PUT -H "Accept:application/json"\
            -H "Content-Type:application/json" "http://$worker_addr:10006/connectors/$connector/config" \
            -d  @- <<EOF
{
    "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
    
    "tasks.max": 12,
    "topics": "$topic",
    
    "connection.url": "$connection_url",
    "connection.user": "$connection_user",
    "connection.password": "$connection_password",

    "db.timezone": "UTC",
    "insert.mode": "upsert",
    "pk.mode": "record_value",
    "pk.fields": "generation_time, server_id",

    "batch.size": 1000,
    
    "table.name.format": "${topic//./_}",
    
    "max.retries": 4,
    "retry.backoff.ms": 3000,
    "connection.attempts": 4
}
EOF
done