'''
Task
You are given a 2-D array with dimensions X.
Your task is to perform the  tool over axis  and then find the  of that result.

Input Format
The first line of input contains space separated values of  and .
The next  lines contains  space separated integers.

Output Format
Compute the sum along axis . Then, print the product of that sum.
'''

import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for i in range(N)], int)
print(numpy.prod(numpy.sum(A, axis=0)))
