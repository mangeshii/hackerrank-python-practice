'''
Task
You are given two arrays  and . Both have dimensions of X.
Your task is to compute their matrix product.

Input Format
The first line contains the integer .
The next  lines contains  space separated integers of array .
The following  lines contains  space separated integers of array .

Output Format
Print the matrix multiplication of  and .
'''

import numpy
n = int(input())
A = numpy.array([list(map(int, input().split())) for n in range(n)])
B = numpy.array([list(map(int, input().split())) for n in range(n)])

print(numpy.dot(A, B))
