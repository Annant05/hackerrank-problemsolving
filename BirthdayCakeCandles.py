#!/bin/python3

#URL : https://www.hackerrank.com/challenges/birthday-cake-candles/problem

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max_elem = max(ar)
    count = 0
    # You may use this
    # count = ar.count( max_elem )
    for elem in ar:
        if (elem == max_elem):
            count +=1
    return (count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
