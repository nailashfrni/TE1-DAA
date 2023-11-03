from BCIS import *
from counting_sort import *
from util_functions import *
import time

sizes = ['small', 'mid', 'large']
versions = ['random', 'sorted', 'reversed']

for size in sizes:
    print("======================= " + size.upper() + " =======================")

    for version in versions:
        array = file_to_array(f'dataset/{size}/{version}.txt')
        
        print('- ' + version.upper() + ' VERSION -')
        # BCIS
        start = time.time()
        BCIS(array, 0, len(array) - 1)
        end = time.time()
        print('BCIS: ', (end - start) * 1000, 'ms')

        # Counting
        start = time.time()
        counting_sort(array)
        end = time.time()
        print('Counting Sort: ', (end - start) * 1000, 'ms')
        print()