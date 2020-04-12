'''
A deque is a double-ended queue. It can be used to add or remove elements from both ends.
Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same  performance in either direction.

Task
Perform append, pop, popleft and appendleft methods on an empty deque .

Input Format
The first line contains an integer , the number of operations.
The next  lines contains the space separated names of methods and their values.

Output Format
Print the space separated elements of deque .
'''

from collections import deque

d = deque()
n = int(input())

for i in range(n):
    s = input().split()

    if s[0] == 'append':
        d.append(s[1])
    elif s[0] == 'appendleft':
        d.appendleft(s[1])
    elif s[0] == 'pop':
        d.pop()
    elif s[0] == 'popleft':
        d.popleft()

print(*d)
