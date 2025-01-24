import csv
import multiprocessing
import os
import hashlib

DEBUG = True
HASH_SEED = b"ABC"
BATCH_SIZE = 10_000
AUTO_REMOVE = True

def main(): 
    num_rows_options = [1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]

    with multiprocessing.Pool() as pool: 
        pool.map(populate_csv, num_rows_options)


def populate_csv(num_rows): 
    data = []
    file_name = f"{num_rows}_rows.csv"
    debug_print(f"Populating csv {file_name}")
    
    if AUTO_REMOVE:
        debug_print(f"Autoremove enabled, removing file")
        try:
            os.remove(file_name)
        except:
            pass     

    with open(file_name, "w") as f:
        writer = csv.writer(f)
        
        num_loops = 1
        if BATCH_SIZE < num_rows:
            num_loops = num_rows // BATCH_SIZE
        debug_print(f"Using {num_loops} loops for batch size {BATCH_SIZE}")
        running_total = 0
        for _ in range(num_loops):
            data = []
            for i in range(BATCH_SIZE):
                data.append(hashlib.sha256(HASH_SEED + str(running_total + i).encode()).hexdigest())
            running_total += BATCH_SIZE
            writer.writerows(data)
            debug_print(f"Wrote {BATCH_SIZE} rows for a total of {running_total} records")

def debug_print(formatted_str):
    pid = os.getpid()
    if DEBUG:
        print(f"{pid}:", formatted_str)


main()
