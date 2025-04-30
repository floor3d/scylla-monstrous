### Asynchronous looping queries: Hello, Universe
We are now making some serious improvements. When we query asynchronously, there
is no blocking -- we can essentially make a massive amount of statements at almost
the same time, and then resolve them all at once. Resolving them isn't immediate,
but it's quicker than taking one query at a time and resolving it individually, 
because you don't have to wait for the past query to be finished.

ScyllaDB thrives on concurrency and high-read scenarios. If you give it a bunch of
different queries at once, it'll handle them with flying colors.

The code for querying data from ScyllaDB is in `query.py`, and the code to 
test the speeds of this implementation is in `benchmark.py`.
