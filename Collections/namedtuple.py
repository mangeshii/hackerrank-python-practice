'''
Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.


Task
Dr. John Wesley has a spreadsheet containing a list of student's , ,  and .
Your task is to help Dr. Wesley calculate the average marks of the students.

Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format
The first line contains an integer , the total number of students.
The second line contains the names of the columns in any order.
The next  lines contains the , ,  and , under their respective column names.

Output Format
Print the average marks of the list corrected to 2 decimal places.
'''

from collections import namedtuple

n = int(input())
fields = input()

students = namedtuple('students', fields)
total_marks = 0

for i in range(n):
    IDs, marks, name, classs = input().split()

    s = students(IDs, marks, name, classs)

    total_marks += int(s.MARKS)
print('{:2f}'.format(total_marks/(n)))
