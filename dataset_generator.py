import random

SMALL_SIZE = 500
MID_SIZE = 5000
LARGE_SIZE = 50000

def generate_dataset(size, str_size):
    with open(f'dataset/{str_size}/random.txt', 'w') as small_rand_f:
        array = []
        for i in range(size):
            temp = random.randint(0, size)
            array.append(temp)
            small_rand_f.write(str(temp) + "\n")

    with open(f'dataset/{str_size}/sorted.txt', 'w') as small_sort_f:
        array.sort()
        for item in array:
            small_sort_f.write(str(item) + "\n")

    with open(f'dataset/{str_size}/reversed.txt', 'w') as small_reversed_f:
        array.reverse()
        for item in array:
            small_reversed_f.write(str(item) + "\n")

if __name__ == '__main__':
    random.seed(42)
    generate_dataset(SMALL_SIZE, 'small')
    generate_dataset(MID_SIZE, 'mid')
    generate_dataset(LARGE_SIZE, 'large')