# 백준 10816
""" 
입력:
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

출력:
3 0 0 1 2 0 0 2
"""

n = int(input())
array = sorted(list(map(int, input().split())))
m = int(input())
array2 = list(map(int, input().split()))

count = {}

for i in array:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1


def bs(array, target, start, end):
    if start > end:
        return 0

    middle = (start + end) // 2

    if array[middle] == target:
        return count.get(target)
    elif array[middle] < target:
        return bs(array, target, start, middle - 1)
    else:
        return bs(array, target, middle + 1, end)


for j in array2:
    print(bs(array, j, 0, len(array) - 1), end=" ")
