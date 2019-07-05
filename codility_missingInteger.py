# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import array


def solution(A):
    # write your code in Python 3.6
    a = array.array('B', [0] * 10**8)
    b = array.array('B', [0] * 10**8)
    c = array.array('B', [0] * 10**8)
    sequence = 0
    
    
    for el in A:
        if el<=0:
            continue
        else:
            if el <= 1000000:
                a[el] = 1
            else:
                continue
    
    res = 1
    while(1):
        if a[res] == 0:
            return res
        else:
            res += 1
    return res
