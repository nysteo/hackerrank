
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minSum = 0
    maxSum = 0
    minNumber = 10000
    maxNumber = 0

    for x in range(len(arr)):
        if arr[x] < minNumber:
            minNumber = arr[x]
        elif arr[x] > maxNumber:
            maxNumber = arr[x]
    for x in range(len(arr)):
        if(arr[x] != minNumber):
            minSum = minSum + arr[x]
        if(arr[x] != maxNumber):
            maxSum = maxSum + arr[x]
    print(maxSum, minSum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
