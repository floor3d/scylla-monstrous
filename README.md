## Monstrously Fast ScyllaDB Driver Performance Guidelines

This repository will outline how to get the most out of the monstrous querying
speed capabilities of the NoSQL database, ScyllaDB. 

In particular, it outlines different ways of making a lot of simple queries at once.

The example query that we want to perform is as such:

`SELECT * FROM users WHERE id = ?`

where `?` is one of `n` IDs that we want to search for.

We will be testing a lot of different ways to do this, and providing benchmarks
for each. We will be making permutations of the following tactics:

1. Simple `IN` statement
2. Simple, looped, single queries
3. Multithreading
4. Prepared statements
5. Asynchronous queries
6. Concurrent queries
7. Multiprocessing

To test our permutations, we will have benchmarking scripts. We will test everything
from searching only for one record, to hundreds, to thousands, to tens and hundreds of
thousands of records, in databases from hundreds, to thousands, to millions, to billions
of rows.

ScyllaDB makes confident assurances in their `Why ScyllaDB` article 
[as shown here](https://docs.scylladb.com/stable/get-started/why-scylladb/),
and we will prove that those assurances are not made up. ScyllaDB is truly 
monstrously fast, and by running through different query methods, we will find the
best way to take advantage of it.

### Important note
This repository uses specifically the Python driver for ScyllaDB, and as a result,
benchmarks might change a lot depending on which driver is used. For example, due to
the Python GIL, multiprocessing has much greater performance impacts than 
multithreading -- this may change for other languages. Take these benchmarks and
strategies with a grain of salt.
