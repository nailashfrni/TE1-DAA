from util_functions import *
import math

def BCIS(array, left, right):
    SL = left
    SR = right
    while SL < SR:
        # penentuan posisi LC dan RC
        swap(array, SR, SL + ((SR - SL) // 2))
        if array[SL] == array[SR]:
            if is_equal(array, SL, SR) == -1:
                return
        if array[SL] > array[SR]:
            swap(array, SL, SR)
        if (SR - SL) >= 100:
            for i in range(SL + 1, int(math.sqrt(SR - SL)) + 1):
                if array[SR] < array[i]:
                    swap(array, SR, i)
                elif array[SL] > array[i]:
                    swap(array, SL, i)
        i = SL + 1

        LC = array[SL]
        RC = array[SR]

        # main code on sort trip
        while i < SR:
            curr_item = array[i]
            if curr_item >= RC:
                array[i] = array[SR - 1]
                insright(array, curr_item, SR, right)
                SR -= 1
            elif curr_item <= LC:
                array[i] = array[SL + 1]
                insleft(array, curr_item, SL, left)
                SL += 1
                i += 1
            else:
                i += 1
        SL += 1
        SR -= 1    
        
if __name__ == '__main__':
    lst = file_to_array('dataset/small/random.txt')
    BCIS(lst, 0, len(lst) - 1)
    print(lst)