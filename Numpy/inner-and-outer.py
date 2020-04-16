'''
Task
You are given two arrays:  and .
Your task is to compute their inner and outer product.

Input Format
The first line contains the space separated elements of array .
The second line contains the space separated elements of array .

Output Format
First, print the inner product.
'''

import numpy
A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)

print(numpy.inner(A, B))
print(numpy.outer(A, B))
