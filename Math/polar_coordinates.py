'''
Task
You are given a complex . Your task is to convert it to polar coordinates.

Input Format
A single line containing the complex number . Note: complex() function can be used in python to convert the input as a complex number.

Output Format
Output two lines:
The first line should contain the value of .
The second line should contain the value of .
'''

import cmath

z = complex(input())
w = cmath.polar(z)
print(*w, sep="\n")
