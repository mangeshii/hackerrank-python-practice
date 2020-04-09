'''
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

Task
You are given a two lists A and B.Your task is to compute their cartesian product A X B.

Input Format
The first line contains the space separated elements of list .
The second line contains the space separated elements of list .
Both lists have no duplicate integer elements.

Output Format
Output the space separated tuples of the cartesian product.
'''

from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print((*product(a, b)))
