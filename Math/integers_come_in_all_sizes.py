'''
Task
Read four numbers, a, b, c, and d, and print the result of a^b +c^d.

Input Format
Integers a,b,c, and d are given on four separate lines, respectively.

Output Format
Print the result of a^b +c^d on one line.
'''

a=int(input())
b=int(input())
c=int(input())
d=int(input())

x=('{}'.format(pow(a,b)+pow(c,d)))
print(x)
