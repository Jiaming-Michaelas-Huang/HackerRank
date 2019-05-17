
import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap_count = 0;
    for i in range(0,len(arr)):
        while arr[i] != i+1:
            pos = arr[i] - 1
            temp = arr[pos]
            arr[pos] = arr[i]
            arr[i] = temp
            swap_count = swap_count + 1
    return swap_count





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()