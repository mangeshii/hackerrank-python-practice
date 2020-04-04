'''
TASK
You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .
Your task is to execute those operations and print the sum of elements from set .

Input Format
The first line contains the number of elements in set .
The second line contains the space separated list of elements in set .
The third line contains integer , the number of other sets.
The next  lines are divided into  parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

Output Format
Output the sum of elements in set .
'''

length = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    (operation_name, other_set_length) = input().split()
    other_set = set(map(int, input().split()))

    if operation_name == 'intersection_update':
        A.intersection_update(other_set)
    elif operation_name == 'update':
        A.update(other_set)
    elif operation_name == 'symmetric_difference_update':
        A.symmetric_difference_update(other_set)
    elif operation_name == 'difference_update':
        A.difference_update(other_set)
    else:
        assert False

print(sum(A))
