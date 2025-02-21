import csv
import multiprocessing
import os
import hashlib

DEBUG = False
HASH_SEED = b"ABC"
BATCH_SIZE = 10_000
AUTO_REMOVE = True
DIR_NAME = "csvs"

def create_dir():
    debug_print(f"Trying to create directory {DIR_NAME} ...")
    try:
        os.mkdir(DIR_NAME)
        print(f"Directory '{DIR_NAME}' created successfully.")
    except FileExistsError:
        print(f"Directory '{DIR_NAME}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{DIR_NAME}'.")

def main(): 
    num_rows_options = [1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
    create_dir()
    with multiprocessing.Pool() as pool: 
        pool.map(populate_csv, num_rows_options)


def populate_csv(num_rows): 
    data = []
    file_name = os.path.join(DIR_NAME, f"{num_rows}_rows.csv")
    debug_print(f"Populating csv {file_name}")
    
    if AUTO_REMOVE:
        debug_print(f"Autoremove enabled, removing file")
        try:
            os.remove(file_name)
        except:
            pass     

    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["hash", "id"])
        
        num_loops = 1
        if BATCH_SIZE < num_rows:
            num_loops = num_rows // BATCH_SIZE
        debug_print(f"Using {num_loops} loops for batch size {BATCH_SIZE} for {num_rows} rows")
        running_total = 0
        counter = 1
        for _ in range(num_loops):
            data = []
            for i in range(min(BATCH_SIZE, num_rows)):
                data.append([hashlib.sha256(HASH_SEED + str(running_total + i).encode()).hexdigest(), counter])
                counter += 1
            running_total += BATCH_SIZE
            writer.writerows(data)
            debug_print(f"Wrote {BATCH_SIZE} rows for a total of {running_total} records")

def debug_print(formatted_str):
    pid = os.getpid()
    if DEBUG:
        print(f"{pid}:", formatted_str)


main()
