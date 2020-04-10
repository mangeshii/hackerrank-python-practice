'''
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function.
You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.
For a better understanding of the problem, check the explanation.

Input Format
A single line of input consisting of the string .

Output Format
A single line of output consisting of the modified string.
'''

from __future__ import print_function
from itertools import groupby

string = raw_input().strip()
for k, v in groupby(string):

    print((len(list(v)), int(k)), end=" ")
