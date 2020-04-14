'''
Input Format
The first line contains  and  separated by a space.
The next  lines contains the space separated marks obtained by students in a particular subject.

Output Format
Print the averages of all students on separate lines.
The averages must be correct up to  decimal place.
'''

m, n = map(int, input().split())


sheet = []
for i in range(n):
    sheet.append(map(float, input().split()))
for j in zip(*sheet):
    print((sum(j))/(n))
