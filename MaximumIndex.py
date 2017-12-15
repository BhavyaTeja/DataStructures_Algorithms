"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

Example :

A : [3 5 4 2]

Output : 2
"""

list = list(map(int, input().split()))

def MaximumIndex(list):
    if len(list) == 0 or len(list) == 1:
        return 0
    else:
        j = len(list) - 1
        i = 0
        result = []
        while i < len(list):
            for j in range(len(list)):
                if list[i] <= list[j]:
                    result.append(j-i)
            i += 1
    return 0 if result == [] else max(result)

print(MaximumIndex(list))



