'''
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of  members per group where  ≠ .

The Captain was given a separate room, and the rest were given one room per group.
Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.
Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of  and the room number list.

Input Format
The first line consists of an integer, , the size of each group.
The second line contains the unordered elements of the room number list.

Output Format
Output the Captain's room number.
'''

k = int(input())
elements = list(map(int, input().split()))

my_set = set(elements)

my_set_sum = sum(my_set)
elements_sum = sum(elements)

diff = my_set_sum*k - elements_sum

print(diff//(k-1))
