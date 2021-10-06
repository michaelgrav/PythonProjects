#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    count = 0
    # Write your code here
    for i in range(0, n):
        num1 = ar[i]
        for j in range(i, n + 1):
            num2 = ar[j]
            sum = num1 + num2
            if sum % k == 0:
                count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
    num1: 1 num2: 2

    num1: 1 num2: 2

    num1: 3 num2: 3

    num1: 3 num2: 6

    num1: 2 num2: 1

    num1: 6 num2: 6

    num1: 1 num2: 2"""