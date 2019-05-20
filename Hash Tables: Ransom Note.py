#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dic = {}
    for word in magazine:
        dic.setdefault(word,0)
        dic[word] += 1
    for word in note:
        if word in dic:
            if dic[word] == 0:
                print "No"
                return
            dic[word] -= 1
        else:
            print "No"
            return
    print "Yes"
    return


if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)