import random
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import argparse
from time import time
import threading

def connect_to_scylla():
    cluster = Cluster(['127.0.0.1'])  
    session = cluster.connect('ks')  
    return session


def worker(session, user_ids, table_name, shared_ret, id):
    ret = []
    for user_id in user_ids:
        query = f"SELECT * FROM {table_name} WHERE id = {user_id}"
        stmt = SimpleStatement(query)
        result = session.execute(stmt)
        ret.append(result)
    shared_ret[id] = ret


def query_user_threaded(session, user_ids, table_name, num_threads):
    threads = []
    shared_ret = [[] for _ in range(len(user_ids))]
    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(session, user_ids[i], table_name, shared_ret, i))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return [item for sublist in shared_ret for item in sublist]


def generate_random_ids(total_users, num_to_query):
    return random.sample(range(1, total_users + 1), num_to_query)


def go(total_users, num_to_query, table_name, num_threads):
    session = connect_to_scylla()
    random_ids = generate_random_ids(total_users, num_to_query)

    batched_ids_for_threading = [random_ids[i::num_threads] for i in range(num_threads)]
    start = time()
    rows = query_user_threaded(session, batched_ids_for_threading, table_name, num_threads)
    end = time()

    diff = end - start

    str_diff = f"{diff:0.4f}"
    print(f"Queried {num_to_query} users out of {total_users} from table {table_name} in {str_diff} seconds")
    
    session.shutdown()
    
    return (str_diff, rows)

parser = argparse.ArgumentParser(description='Query Scylla for random users')
parser.add_argument('--total_users', type=int, required=True, help='Total number of users in the database')
parser.add_argument('--num_to_query', type=int, required=True, help='Number of users to query')
parser.add_argument('--table_name', type=str, required=True, help='Table name to query from')
parser.add_argument('--num_threads', type=int, required=True, help='How many threads to use')

args = parser.parse_args()

go(args.total_users, args.num_to_query, args.table_name, args.num_threads)   
