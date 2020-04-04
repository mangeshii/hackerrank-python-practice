'''
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

Task
Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Input Format
The first line contains the integer, , the total number of plants.
The second line contains the  space separated heights of the plants.

Output Format
Output the average height value on a single line.
'''


def average(array):
    k = set(arr)

    w = sum(k) / len(k)
    return w


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
