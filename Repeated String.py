#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    len_str = len(s)
    a_count = 0
    for j in s:
        if j == 'a':
            a_count = a_count+1
    times = int(n/len_str)
    whole_a = times*a_count
    residual = n - len_str*times
    for i in range(0,residual,1):
        if(s[i] == 'a'):
            whole_a = whole_a + 1
    return whole_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
