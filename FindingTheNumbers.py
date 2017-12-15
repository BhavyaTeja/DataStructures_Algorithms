"""
You are given an array A containing 2*N+2 positive numbers, out of which N numbers are repeated exactly once
and the other two numbers occur exactly once and are distinct. You need to find the other two numbers
and print them in ascending order.

"""

array = list(map(int, input().split()))



def FindingNumers(array):
    dict = {}
    for i in array:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    keys = [i for i, j in dict.items() if j == 1]
    return keys

print(FindingNumers(array))


