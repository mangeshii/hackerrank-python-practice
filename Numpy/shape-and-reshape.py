'''
Task
You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.

Input Format
A single line of input containing  space separated integers.

Output Format
Print the X NumPy array.
'''

import numpy
n = list(map(int, input().split()))
my_array = numpy.array([n])
x = numpy.reshape(my_array, (3, 3))
print(x)
