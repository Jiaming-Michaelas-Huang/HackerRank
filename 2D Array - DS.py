
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_hourglassSum = -99999
    for i in range(1,5):
        for j in range(1,5):
            hourglasssum = arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
            if hourglasssum > max_hourglassSum :
                max_hourglassSum = hourglasssum
    return  max_hourglassSum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()