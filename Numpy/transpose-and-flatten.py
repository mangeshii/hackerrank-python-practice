'''
Task
You are given a X integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results.

Input Format
The first line contains the space separated values of  and .
The next  lines contains the space separated elements of  columns.

Output Format
First, print the transpose array and then print the flatten.
'''

import numpy
n, m = (input().split())
lines = []
for i in range(int(n)):
    lines.append(input().split())

my_array = numpy.array(lines, int)

print(numpy.transpose(my_array), sep="\n")
print(my_array.flatten())
