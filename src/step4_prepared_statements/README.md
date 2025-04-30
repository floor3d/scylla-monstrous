### Prepared Statements: A solid step
Prepared statements are great for many queries of the same kind.

The database can, from a high level, be "prepared" for the further queries. Normally, databases
like Scylla need to perform some optimizations on your queries when you submit them; with prepared statements,
it does not have to perform the same optimizations over and over; it only needs to perform them once!

The code for querying data from ScyllaDB is in `query.py`, and the code to 
test the speeds of this implementation is in `benchmark.py`.
