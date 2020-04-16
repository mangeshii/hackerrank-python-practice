'''
Task
You are given a 2-D array with dimensions X.
Your task is to perform the min function over axis  and then find the max of that.

Input Format
The first line of input contains the space separated values of  and .
The next  lines contains  space separated integers.

Output Format
Compute the min along axis  and then print the max of that result.

'''
import numpy
n, m = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for n in range(n)])

x = (numpy.min(A, axis=1))
print(max(x))
