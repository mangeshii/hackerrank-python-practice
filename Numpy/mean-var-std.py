'''
Task
You are given a 2-D array of size X.
Your task is to find:
The mean along axis 
The var along axis 
The std along axis 

Input Format
The first line contains the space separated values of  and .
The next  lines contains  space separated integers.

Output Format
First, print the mean.
Second, print the var.
Third, print the std.

'''
import numpy
n, m = map(int, input().split(" "))

A = numpy.array([list(map(int, input().split())) for i in range(n)])
print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
print(numpy.std(A))
