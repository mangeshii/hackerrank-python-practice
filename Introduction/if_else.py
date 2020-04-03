'''
Task
Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird

Input Format
A single line containing a positive integer, .

Output Format
Print Weird if the number is weird; otherwise, print Not Weird.
'''


import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    a = n % 2

    if a != 0:
        print('Weird')
    elif a == 0 and (2 <= n <= 5):
        print('Not Weird')
    elif a == 0 and (6 <= n <= 20):
        print('Weird')
    elif a == 0 and (n > 20):
        print('Not Weird')
