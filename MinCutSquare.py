"""
Given a paper of size A x B. Task is to cut the paper into squares of any size. Find the minimum number of squares that can be cut from the paper.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains two integer A and B denoting the two size of the paper.

Output:
Print the minimum number of squares that can be cut from the paper.
"""

length, breadth = (map(int, input().split()))


def MinCutSquare(length, breadth):
    count = 0
    temp = 0
    if length < breadth:
        while length > 0:
            temp = breadth % length
            count += breadth // length
            breadth = length
            length = temp
    else:
        while breadth > 0:
            temp = length % breadth
            count += length // breadth
            length = breadth
            breadth = temp
    return count

print(MinCutSquare(length, breadth))