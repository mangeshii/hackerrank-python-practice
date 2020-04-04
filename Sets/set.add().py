'''
Task
Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.
Find the total number of distinct country stamps.

Input Format
The first line contains an integer , the total number of country stamps.
The next  lines contains the name of the country where the stamp is from.

Output Format
Output the total number of distinct country stamps on a single line.
'''

NoOfStamps = int(input())
country = set()

for i in range(NoOfStamps):
    country.add(input())
print(len(country))
#x=set(country)
