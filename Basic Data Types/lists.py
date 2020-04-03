'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format
The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Output Format
For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

'''

if __name__ == '__main__':
    N = int(input())
    result = []
    for n in range(N):
        x = input().split(" ")

        if x[0] == 'append':
            result.append(int(x[1]))
        if x[0] == 'print':
            print(result)
        if x[0] == 'insert':
            result.insert(int(x[1]), int(x[2]))
        if x[0] == 'reverse':
            result.reverse()
        if x[0] == 'pop':
            result.pop()
        if x[0] == 'sort':
            result.sort()
        if x[0] == 'remove':
            result.remove(int(x[1]))
       
