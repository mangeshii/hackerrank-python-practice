'''
This tool returns successive  length permutations of elements in an iterable.
If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.
Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

Task
You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

Input Format
A single line containing the space separated string  and the integer value .

Output Format
Print the permutations of the string  on separate lines.
'''

from itertools import permutations

s = list(input().split())

for i in sorted(permutations(s[0], int(s[1]))):
    print(''.join(i))
