import random
from cassandra.cluster import Cluster
import argparse
from time import time

def connect_to_scylla():
    cluster = Cluster(['127.0.0.1'])  
    session = cluster.connect('ks')  
    return session


def query_user(session, prep, user_id):
    bound = prep.bind([user_id])
    return session.execute(bound)


def generate_random_ids(total_users, num_to_query):
    return random.sample(range(1, total_users + 1), num_to_query)


def go(total_users, num_to_query, table_name):
    session = connect_to_scylla()
    random_ids = generate_random_ids(total_users, num_to_query)

    start = time()
    query = session.prepare(f"SELECT * FROM {table_name} WHERE id=?")
    rows = [query_user(session, query, user_id ) for user_id in random_ids]
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

args = parser.parse_args()

go(args.total_users, args.num_to_query, args.table_name)   
