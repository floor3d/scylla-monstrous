CREATE KEYSPACE IF NOT EXISTS ks WITH replication = {'class':'SimpleStrategy', 'replication_factor':1};
CREATE TABLE IF NOT EXISTS ks.table_a (hash text PRIMARY KEY, id bigint);
CREATE TABLE IF NOT EXISTS ks.table_b (hash text PRIMARY KEY, id bigint);
CREATE TABLE IF NOT EXISTS ks.table_c (hash text PRIMARY KEY, id bigint);
CREATE TABLE IF NOT EXISTS ks.table_d (hash text PRIMARY KEY, id bigint);
CREATE TABLE IF NOT EXISTS ks.table_e (hash text PRIMARY KEY, id bigint);
CREATE TABLE IF NOT EXISTS ks.table_f (hash text PRIMARY KEY, id bigint);


COPY ks.table_a FROM '/1000_rows.csv'      WITH HEADER=TRUE;
COPY ks.table_b FROM '/10000_rows.csv'     WITH HEADER=TRUE;
COPY ks.table_c FROM '/100000_rows.csv'    WITH HEADER=TRUE;
COPY ks.table_d FROM '/1000000_rows.csv'   WITH HEADER=TRUE;
COPY ks.table_e FROM '/10000000_rows.csv'  WITH HEADER=TRUE;
COPY ks.table_f FROM '/100000000_rows.csv' WITH HEADER=TRUE;
