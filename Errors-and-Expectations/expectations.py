'''
Task
You are given two values  and .
Perform integer division and print .

Input Format
The first line contains , the number of test cases.
The next  lines each contain the space separated values of  and .

Output Format
Print the value of .
In the case of ZeroDivisionError or ValueError, print the error code.
'''

T = int(input())

for i in range(0, T):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

