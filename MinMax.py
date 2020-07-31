#!/bin/python3

#URL : https://www.hackerrank.com/challenges/mini-max-sum/problem

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)
    sum_max = 0 
    sum_min = 0
    arr_len = len(arr)
    arr_offset = 1

    for index in range(arr_len):
        if( index + arr_offset ) == arr_len:
            break
        sum_min += arr[index]
        sum_max += arr[arr_len-(1+index)]
    print(sum_min,sum_max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
