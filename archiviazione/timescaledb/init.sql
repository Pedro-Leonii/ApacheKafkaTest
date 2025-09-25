CREATE DATABASE kafka;

\c kafka

CREATE DOMAIN unsigned_int AS integer CHECK (VALUE > 0);

CREATE DOMAIN cpu_percentage AS int CHECK (VALUE > 0 AND VALUE < 100);

CREATE TABLE servers_logs_access(
    server_id varchar(255) NOT NULL,
    generation_time timestamp NOT NULL,
    user_ip varchar(45) NOT NULL,
    username varchar(255),
    request_url varchar(1000),
    request_method varchar(10) NOT NULL,
    response_status_code unsigned_int NOT NULL,
    response_dim unsigned_int NOT NULL,
    user_agent varchar(300) NOT NULL,
    PRIMARY KEY (generation_time, server_id)
)
WITH(
    tsdb.hypertable=true,
    tsdb.partition_column='generation_time',
    tsdb.chunk_interval='1d',
    tsdb.segmentby='server_id'
);

CALL add_columnstore_policy('servers_logs_access', after => INTERVAL '1d');

CREATE TABLE servers_logs_application(
    server_id varchar(255) NOT NULL,
    generation_time timestamp NOT NULL,
    severity varchar(10) NOT NULL,
    msg varchar(500) NOT NULL,
    source_thread varchar(100) NOT NULL,
    source_class varchar(100) NOT NULL,
    PRIMARY KEY (generation_time, server_id)

)
WITH(
    tsdb.hypertable=true,
    tsdb.partition_column='generation_time',
    tsdb.chunk_interval='1d',
    tsdb.segmentby='server_id'
);

CALL add_columnstore_policy('servers_logs_application', after => INTERVAL '1d');

CREATE TABLE servers_metrics(
    server_id varchar(255) NOT NULL,
    generation_time timestamp NOT NULL,
    cpu_usage cpu_percentage NOT NULL,
    running_threads unsigned_int NOT NULL,
    current_users unsigned_int NOT NULL,
    open_files unsigned_int NOT NULL,
    PRIMARY KEY (generation_time, server_id)
)
WITH(
    tsdb.hypertable=true,
    tsdb.partition_column='generation_time',
    tsdb.chunk_interval='1d',
    tsdb.segmentby='server_id'
);

CALL add_columnstore_policy('servers_metrics', after => INTERVAL '1d');

