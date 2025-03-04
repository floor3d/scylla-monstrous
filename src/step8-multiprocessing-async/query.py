import random
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import argparse
from time import time
from multiprocessing import Pool

def connect_to_scylla():
    cluster = Cluster(['127.0.0.1'])  
    session = cluster.connect('ks')  
    return session


def query_user(user_ids, table_name):
    session = connect_to_scylla()
    futures = []
    for user_id in user_ids:
        query = f"SELECT * FROM {table_name} WHERE id = {user_id}"
        stmt = SimpleStatement(query)
        futures.append(session.execute_async(stmt))
    results = [f.result().one()[1] for f in futures]
    session.shutdown()
    return results


def generate_random_ids(total_users, num_to_query):
    return random.sample(range(1, total_users + 1), num_to_query)


def multiprocess(values, table_name, process_count=10):
    with Pool(processes=process_count) as pool:
        chunk_size = min(len(values) // process_count + 1, len(values))
        if chunk_size == 0:
            return []
        chunks = [(values[i:i + chunk_size],table_name) for i in range(0, len(values), chunk_size)]
        results = []
        for mapped_result in pool.starmap(query_user, chunks):
            results.extend(mapped_result)
    return results


def go(total_users, num_to_query, table_name):
    random_ids = generate_random_ids(total_users, num_to_query)

    start = time()
    rows = multiprocess(random_ids, table_name)
    end = time()

    diff = end - start

    str_diff = f"{diff:0.4f}"
    print(f"Queried {num_to_query} users out of {total_users} from table {table_name} in {str_diff} seconds")
    
    return (str_diff, rows)

parser = argparse.ArgumentParser(description='Query Scylla for random users')
parser.add_argument('--total_users', type=int, required=True, help='Total number of users in the database')
parser.add_argument('--num_to_query', type=int, required=True, help='Number of users to query')
parser.add_argument('--table_name', type=str, required=True, help='Table name to query from')

args = parser.parse_args()

go(args.total_users, args.num_to_query, args.table_name)   
