CREATE KEYSPACE IF NOT EXISTS ks WITH replication = {'class':'SimpleStrategy', 'replication_factor':1};
CREATE TABLE IF NOT EXISTS ks.table_a (id bigint PRIMARY KEY, hash text);
CREATE TABLE IF NOT EXISTS ks.table_b (id bigint PRIMARY KEY, hash text);
CREATE TABLE IF NOT EXISTS ks.table_c (id bigint PRIMARY KEY, hash text);
CREATE TABLE IF NOT EXISTS ks.table_d (id bigint PRIMARY KEY, hash text);
CREATE TABLE IF NOT EXISTS ks.table_e (id bigint PRIMARY KEY, hash text);
CREATE TABLE IF NOT EXISTS ks.table_f (id bigint PRIMARY KEY, hash text);


COPY ks.table_a FROM 'csvs/1000_rows.csv'      WITH HEADER=TRUE;
COPY ks.table_b FROM 'csvs/10000_rows.csv'     WITH HEADER=TRUE;
COPY ks.table_c FROM 'csvs/100000_rows.csv'    WITH HEADER=TRUE;
COPY ks.table_d FROM 'csvs/1000000_rows.csv'   WITH HEADER=TRUE;
COPY ks.table_e FROM 'csvs/10000000_rows.csv'  WITH HEADER=TRUE;
COPY ks.table_f FROM 'csvs/100000000_rows.csv' WITH HEADER=TRUE;
