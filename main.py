from BCIS import *
from counting_sort import *
from util_functions import *
import time
import tracemalloc

sizes = ['small', 'mid', 'large']
versions = ['sorted', 'random', 'reversed']

for size in sizes:
    print("======================= " + size.upper() + " =======================")

    for version in versions:
        # Convert dataset file to array
        array = file_to_array(f'dataset/{size}/{version}.txt')
        
        print('- ' + version.upper() + ' VERSION -')
        # BCIS
        # Jalankan tracer time dan memory usage
        tracemalloc.start()
        start = time.time()

        # Jalankan BCIS algorithm
        BCIS(array, 0, len(array) - 1)

        # Hentikan tracer dan tampilkan stats
        end = time.time()
        memory_usage = tracemalloc.get_traced_memory()[1] / 1000000
        tracemalloc.stop()
        print('1. BCIS')
        print('Memory usage: ', memory_usage, 'MB')
        print('Running time: ', (end - start) * 1000, 'ms')

        # Counting
        # Jalankan tracer time dan memory usage
        tracemalloc.start()
        start = time.time()

        # Jalankan counting sort algorithm
        counting_sort(array)

        # Hentikan tracer dan tampilkan stats
        end = time.time()
        memory_usage = tracemalloc.get_traced_memory()[1] / 1000000
        tracemalloc.stop()
        print('2. Counting Sort')
        print('Memory usage: ', memory_usage, 'MB')
        print('Running time: ', (end - start) * 1000, 'ms')
        print()