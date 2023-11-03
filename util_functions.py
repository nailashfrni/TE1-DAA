def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def is_equal(array, SL, SR):
    for k in range(SL + 1, SR):
        if array[k] != array[SL]:
            swap(array, k, SL)
            return k
    return -1

def insright(array, curr_item, SR, right):
    j = SR
    while j <= right and curr_item > array[j]:
        array[j - 1] = array[j]
        j += 1
    array[j - 1] = curr_item

def insleft(array, curr_item, SL, left):
    j = SL
    while j >= left and curr_item < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = curr_item

def file_to_array(filename):
    lst = []
    with open(filename, 'r') as file:
        for item in file:
            lst.append(int(item.strip()))
    return lst