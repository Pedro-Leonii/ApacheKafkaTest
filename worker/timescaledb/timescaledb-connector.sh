worker_addr=$1
connection_password=$2
connection_url="jdbc:postgresql://timescaledb:8888/kafka"
connection_user="postgres"

topics=(servers.logs.access servers.logs.application servers.metrics)

for topic in ${topics[@]}; do 
    connector="timescaledb-${topic//./-}"
    curl -i -X PUT -H "Accept:application/json"\
            -H "Content-Type:application/json" "http://$worker_addr:8083/connectors/$connector/config" \
            -d  @- <<EOF
{
    "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
    
    "tasks.max": 12,
    "topics": "$topic",
    
    "connection.url": "$connection_url",
    "connection.user": "$connection_user",
    "connection.password": "$connection_password",

    "db.timezone": "Europe/Rome",
    "insert.mode": "upsert",
    "pk.mode": "record_value",
    "pk.fields": "generation_time, server_id",

    "table.name.format": "${topic//./_}"
}
EOF
done