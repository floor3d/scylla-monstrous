### IN statement: False hero
The natural SQL developer's next step is, why not try an `IN` statement? Surely
this is the better way of going about things.

We learn that while this might seem like a good idea, it's not actually performant.

The code for querying data from ScyllaDB is in `query.py`, and the code to 
test the speeds of this implementation is in `benchmark.py`.
