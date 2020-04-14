'''
You are given a string .
Your task is to find out whether  is a valid regex or not.

Input Format
The first line contains integer , the number of test cases.
The next  lines contains the string .

Output Format
Print "True" or "False" for each test case without quotes.
'''

import re

for i in range(int(input())):
    try:
        re.compile(input())
        result = True
    except:
        result = False
    print(result)
