import math
import os
import random
import re
import sys
import numpy as ny

# Complete the rotLeft function below.
def rotLeft(a, d):
    result = range(0, len(a))
    for r in range(0,len(result)):
        if(r+d < len(result)):
            result[r] = a[r+d]
        else:
            result[r] = a[r+d-len(result)]
    return  result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
