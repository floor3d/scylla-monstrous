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


def query_user(chunk):
    session = connect_to_scylla()
    table_name = chunk[1]
    ret = []
    for user_id in chunk[0]:
        query = f"SELECT * FROM {table_name} WHERE id = {user_id}"
        stmt = SimpleStatement(query)
        result = session.execute(stmt)
        ret.append(result.one()[1])
    session.shutdown()
    return ret

def multiprocess(values, table_name, process_count=10):
    with Pool(processes=process_count) as pool:
        chunk_size = min(len(values) // process_count + 1, len(values))
        if chunk_size == 0:
            return []
        chunks = [(values[i:i + chunk_size],table_name) for i in range(0, len(values), chunk_size)]
        result = []
        for mapped_result in pool.map(query_user, chunks):
            result.extend(mapped_result)
    return result
    
def generate_random_ids(total_users, num_to_query):
    return random.sample(range(1, total_users + 1), num_to_query)

def go(total_users, num_to_query, table_name):
    random_ids = generate_random_ids(total_users, num_to_query)
    process_count = 10

    start = time()
    rows = multiprocess(random_ids, table_name, process_count)
    end = time()
    print(rows)

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
