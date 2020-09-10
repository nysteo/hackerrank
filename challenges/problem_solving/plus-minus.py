
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    arrLen = len(arr)
    posNum = 0
    zeroNum = 0
    negNum = 0

    for x in range(arrLen):
        if arr[x] > 0 : 
            posNum = posNum + 1
        elif arr[x] == 0:
            zeroNum = zeroNum + 1
        elif arr[x] < 0:
            negNum = negNum + 1
    
    print(round(float(posNum /arrLen), 6))
    print(round(float(negNum /arrLen), 6))
    print(round(float(zeroNum /arrLen), 6))
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
