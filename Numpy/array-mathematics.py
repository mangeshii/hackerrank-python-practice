'''
Task
You are given two integer arrays,  and  of dimensions X.
Your task is to perform the following operations:

Add ( + )
Subtract ( - )
Multiply ( * )
Integer Division ( / )
Mod ( % )
Power ( ** )

Input Format
The first line contains two space separated integers,  and .
The next  lines contains  space separated integers of array .
The following  lines contains  space separated integers of array .

Output Format
Print the result of each operation in the given order under Task.
'''

import numpy
n, m = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for i in range(n)])
B = numpy.array([list(map(int, input().split())) for i in range(n)])
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A % B)
print(A ** B)
