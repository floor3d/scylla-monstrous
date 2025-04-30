import sys
import os
from step1_looped_queries.query import go as go_step1
from step2_in_statement.query import go as go_step2
from step3_multithreading.query import go as go_step3
from step4_prepared_statements.query import go as go_step4
from step5_async_queries.query import go as go_step5
from step6_concurrent_prepared_statements.query import go as go_step6
from step7_multiprocessing.query import go as go_step7
from step8_multiprocessing_async.query import go as go_step8
from step9_multiprocessing_async_prepared_statements.query import go as go_step9

def print_log(time_in_s, num_to_query, total_users, table_name, desc):
    print(f"[{desc}]:\t{time_in_s}s -- {num_to_query} rows / {total_users} rows in {table_name}")

def main():
    total_users_domain = [('table_a', 1_000), ('table_b',10_000), ('table_c', 100_000), ('table_d', 1_000_000), ('table_e', 10_000_000), ('table_f', 100_000_000)]
    num_to_query_domain = [10, 100, 1_000, 10_000, 100_000, 1_000_000]

    permutations = []
    for total_users in total_users_domain:
        for num_to_query in num_to_query_domain:
            if total_users[1] < num_to_query:
                continue
            permutation = {}
            permutation["table_name"] = total_users[0]
            permutation["total_users"] = total_users[1]
            permutation["num_to_query"] = num_to_query
            permutations.append(permutation)

    for p in permutations:
        total_users = p["total_users"]
        num_to_query = p["num_to_query"]
        table_name = p["table_name"]
        time_in_s, _ = go_step1(total_users, num_to_query, table_name)
        print_log(time_in_s, num_to_query, total_users, table_name, "(1) LOOPED")
        # time_in_s, _ = go_step2(total_users, num_to_query, table_name)
        # print_log(time_in_s, num_to_query, total_users, table_name, "IN STMT")
        time_in_s, _ = go_step3(total_users, num_to_query, table_name)
        print_log(time_in_s, num_to_query, total_users, table_name, "(3) MULTITHREAD")
        time_in_s, _ = go_step4(total_users, num_to_query, table_name)
        print_log(time_in_s, num_to_query, total_users, table_name, "(4) PREP STMT")
        time_in_s, _ = go_step5(total_users, num_to_query, table_name)
        print_log(time_in_s, num_to_query, total_users, table_name, "(5) ASYNC")
        time_in_s, _ = go_step6(total_users, num_to_query, table_name)
        print_log(time_in_s, num_to_query, total_users, table_name, "(6) CONCUR PREP STMTS")
        time_in_s, _ = go_step7(total_users, num_to_query, table_name)
        print_log(time_in_s, num_to_query, total_users, table_name, "(7) MULTIPROC")
        time_in_s, _ = go_step8(total_users, num_to_query, table_name)
        print_log(time_in_s, num_to_query, total_users, table_name, "(8) MULTIPROC ASYNC")
        time_in_s, _ = go_step9(total_users, num_to_query, table_name)
        print_log(time_in_s, num_to_query, total_users, table_name, "(9) MULTIPROC ASYNC PREP STMTS")


"""
1. create permutated list of total_users, num_to_query, table_name; ensuring that total_users < size(table name)
2. for each step: 
    a. Call 'go' with params total_users, num_to_query, table_name
        return (str_diff [time in seconds], rows)
    b. print out [SHORTDESC OF STEP] [time in s] X rows / X total rows in table_name
COPY ks.table_a FROM 'csvs/1000_rows.csv'      WITH HEADER=TRUE;
COPY ks.table_b FROM 'csvs/10000_rows.csv'     WITH HEADER=TRUE;
COPY ks.table_c FROM 'csvs/100000_rows.csv'    WITH HEADER=TRUE;
COPY ks.table_d FROM 'csvs/1000000_rows.csv'   WITH HEADER=TRUE;
COPY ks.table_e FROM 'csvs/10000000_rows.csv'  WITH HEADER=TRUE;
COPY ks.table_f FROM 'csvs/100000000_rows.csv' WITH HEADER=TRUE;
"""

main()
