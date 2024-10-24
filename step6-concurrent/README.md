### Concurrent queries
As we know, ScyllaDB thrives on concurrency and high-read scenarios. As a result, concurrent queries
are perfect, right? They should have better performance than even asynchronous queries!
Or do they?

-- note -- 

This includes prepared statements, because that's how you're supposed to give the data to 
`execute_concurrent`, I think..!

The code for querying data from ScyllaDB is in `query.py`, and the code to 
test the speeds of this implementation is in `benchmark.py`.
