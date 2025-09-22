CREATE DATABASE logs;

\c logs

CREATE TYPE http_method as ENUM ('GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH');

CREATE TYPE http_status_code as ENUM ('100','101','102','103','200','201','202','203','204','205','206','207','208','226','300','301','302','303','304','305','306','307','308','400','401','402','403','404','405','406','407','408','409','410','411','412','413','414','415','416','417','418','421','422','423','424','425','426','428','429','431','451','500','501','502','503','504','505','506','507','508','510','511');

CREATE TYPE log_severity as ENUM ('INFO', 'DEBUG', 'WARNING', 'ERROR');

CREATE DOMAIN unsigned_int AS integer CHECK (VALUE > 0);

CREATE DOMAIN cpu_percentage AS numeric(3,2) CHECK (VALUE > 0);

CREATE TABLE servers_access_logs(
    server_id varchar(255) NOT NULL,
    generation_time timestamp NOT NULL,
    user_ip cidr NOT NULL,
    username varchar(255),
    request_url varchar(1000),
    request_method http_method NOT NULL,
    response_status_code http_status_code NOT NULL,
    response_dim unsigned_int NOT NULL,
    user_agent varchar(300) NOT NULL,
    PRIMARY KEY (generation_time, server_id)
)
WITH(
    tsdb.hypertable,
    tsdb.partition_column='generation_time',
    tsdb.chunk_interval='1d',
    tsdb.segmentedby='server_id'
);

CALL add_columnstore_policy('server_application_logs', after => INTERVAL '1d');

CREATE TABLE servers_application_logs(
    server_id varchar(255) NOT NULL,
    generation_time timestamp NOT NULL,
    severity severity NOT NULL,
    msg varchar(500) NOT NULL,
    source_thread varchar(100) NOT NULL,
    source_class varchar(100) NOT NULL,
    PRIMARY KEY (generation_time, server_id)

)
WITH(
    tsdb.hypertable,
    tsdb.partition_column='generation_time',
    tsdb.chunk_interval='1d',
    tsdb.segmentedby='server_id'
);

CALL add_columnstore_policy('server_application_logs', after => INTERVAL '1d');

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
    tsdb.hypertable,
    tsdb.partition_column='generation_time',
    tsdb.chunk_interval='1d',
    tsdb.segmentedby='server_id'
);

CALL add_columnstore_policy('servers_metrics', after => INTERVAL '1d');

