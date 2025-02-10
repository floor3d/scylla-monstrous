import random
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import argparse
from time import time

def connect_to_scylla():
    cluster = Cluster(['127.0.0.1'])  
    session = cluster.connect('ks')  
    return session


def query_user(session, user_id, table_name):
    query = f"SELECT * FROM {table_name} WHERE id = {user_id}"
    stmt = SimpleStatement(query)
    return session.execute(stmt)


def generate_random_ids(total_users, num_to_query):
    return random.sample(range(1, total_users + 1), num_to_query)


def go(total_users, num_to_query, table_name):
    session = connect_to_scylla()
    random_ids = generate_random_ids(total_users, num_to_query)

    start = time()
    rows = [query_user(session, user_id, table_name) for user_id in random_ids]
    end = time()

    diff = end - start

    str_diff = f"{diff:0.4f}"
    
    session.shutdown()
    
    return (str_diff, rows)

parser = argparse.ArgumentParser(description='Query Scylla for random users')
parser.add_argument('--total_users', type=int, required=True, help='Total number of users in the database')
parser.add_argument('--num_to_query', type=int, required=True, help='Number of users to query')
parser.add_argument('--table_name', type=str, required=True, help='Table name to query from')

args = parser.parse_args()

go(args.total_users, args.num_to_query, args.table_name)   
