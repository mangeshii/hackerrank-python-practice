'''
Task
You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .

Input Format
The first line contains space separated integers ,  and .
The next  lines contains the space separated elements of the  columns.
After that, the next  lines contains the space separated elements of the  columns.
'''

import numpy

a = input().split()
N = int(a[0])
M = int(a[1])
P = int(a[2])
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
aa = []
for i in range(M):
    aa.append(list(map(int, input().split())))
a1 = numpy.array(a)
a2 = numpy.array(aa)
print(numpy.concatenate((a1, a2)))
