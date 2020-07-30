#!/bin/python3

# URL: https://www.hackerrank.com/challenges/plus-minus/problem

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    positives, zeros, negatives = 0, 0, 0
    for num in arr:
        if (num == 0):
            zeros += 1
        elif(num > 0):
            positives += 1
        elif(num < 0):
            negatives += 1
    n = len(arr)
    print(f"{format(positives/n , '.6f')}\n{format(negatives/n , '.6f')}\n{format(zeros/n , '.6f')}")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
