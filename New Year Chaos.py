#!/bin/python

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(queue):
    lastIndex = len(queue) - 1
    swaps = 0
    swaped = False

    # check if the queue is too chaotic
    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            print "Too chaotic"
            return
    # bubble sorting to find the answer
    for i in xrange(0, lastIndex):
        for j in xrange(0, lastIndex):
            if queue[j] > queue[j + 1]:
                temp = queue[j]
                queue[j] = queue[j + 1]
                queue[j + 1] = temp
                swaps += 1
                swaped = True

        if swaped:
            swaped = False
        else:
            break
    print str(swaps)
    return


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
