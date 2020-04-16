'''
Task
You are given a 1-D array, . Your task is to print the ,  and  of all the elements of .

Input Format
A single line of input containing the space separated elements of array .

Output Format
On the first line, print the  of A.
On the second line, print the  of A.
On the third line, print the  of A.
'''

import numpy

A = numpy.array(input().split(), float)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
