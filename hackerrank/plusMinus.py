#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0 
    neg = 0 
    zer = 0 
    for i in range(len(arr)):
        if arr[i] == 0:
            zer += 1
        if arr[i] > 0:
            pos += 1
        if arr[i] < 0:
            neg += 1
    return pos/len(arr), neg/len(arr), zer/len(arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
