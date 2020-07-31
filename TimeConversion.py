#!/bin/python3

#URL : https://www.hackerrank.com/challenges/time-conversion/problem

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #

    hour = int(s[0:2])
    minute = int(s[3:5])
    sec = int(s[6:8])
    mridm = s[8:10]

    # print(hour, minute, sec, mridm)

    if(mridm == "PM"):
        if(hour == 12):
          hour = 12  
        else:
          hour = hour + 12
    elif(mridm == "AM"):
        if(hour == 12):
            hour = 00
            
    # print(hour, minute, sec)    
    return (f'{hour:02d}:{minute:02d}:{sec:02d}')

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
