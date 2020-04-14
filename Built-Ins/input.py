'''
Task
You are given a polynomial  of a single indeterminate (or variable), .
You are also given the values of  and . Your task is to verify if .

Input Format
The first line contains the space separated values of  and .
The second line contains the polynomial .

Output Format
Print True if . Otherwise, print False.
'''

x, k = map(int, input().split())
p = eval(input())

if p == k:
    print(True)
else:
    print(False)
