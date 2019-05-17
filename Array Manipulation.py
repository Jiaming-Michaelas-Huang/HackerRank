import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    max_result = 0;
    x = 0
    result = [0]*n
    for q in queries:
        start = q[0]-1
        end = q[1]-1
        increment = q[2]
        result[start] = result[start] + increment
        if(end+1<n):
            result[end+1] =result[end+1]-increment
    for i in result:
        x = x + i;
        if (max_result < x): max_result = x;
    return max_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()