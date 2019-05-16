#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n,c):
    step = 0
    count = 0
    while step < n:
        if step + 2 >= n-1:
            count = count + 1
            break
        if c[step+2] == 0:
            step = step + 2
        else:
            step = step + 1
        count = count + 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(n,c)

    fptr.write(str(result) + '\n')

    fptr.close()