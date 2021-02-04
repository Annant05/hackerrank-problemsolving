#!/bin/python3

#URL = https://www.hackerrank.com/challenges/staircase/problem

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    final_pattern = ""
    str_to_add = "#"
    for num in range (n+1):
        if (num == 0 ):
            continue
        pat= " "*(n-num) + str_to_add*(num) + "\n"
        final_pattern += pat
    
        # final_pattern[]
    print (final_pattern[:-1])


if __name__ == '__main__':
    n = int(input())

    staircase(n)
