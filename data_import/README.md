### Data import

This section is to populate your ScyllaDB instance with data to test with.

We will create several database tables, ranging from a very small amount of records
(thousands) to a somewhat large amount (up to a hundred million) so that we can benchmark properly.

Note that this is not a great way of doing things; in a perfect world, for perfect 
results, we would have different Scylla in different compters with all different
table sizes, so as to not have everything on the same instance. In a perfect world,
we would also be using a three-or-more-container Scylla instance.
Similarly, in a perfect world, I'd have ten Dell PowerEdge R760s, a 24-port managed
switch, a Palo Alto firewall, a Cisco firewall, no electricity bill, and a billion
dollars. 
So, we will have to deal with this naive way of benchmarking.

Use `create-data.py` to create the CSV files, and `import-data.sh` to import the CSVs
into Scylla.

Note that it is quicker to copy from a CSV than to import data via queries.


