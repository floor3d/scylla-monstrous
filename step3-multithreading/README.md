### Multithreaded queries: Hello, World, but better
Multithreading is known to speed up any task in programming. In a surprise to no one, it speeds up
our querying, too! It gives a nice performance boost, but still doesn't take advantage of absolutely 
everything that Scylla offers us.

The code for querying data from ScyllaDB is in `query.py`, and the code to 
test the speeds of this implementation is in `benchmark.py`.
