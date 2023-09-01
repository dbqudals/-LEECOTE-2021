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
array1 = sorted(list(map(int, input().split())))
m = int(input())
array2 = list(map(int, input().split()))

# 시간초과
count = {}
""" 
for i in range(len(array2) - 1):
    count[array2[i]] = array1.count(array2[i])

print(list(count.values()))
"""
# 딕셔너리
# count = {}
""" 
for i in array1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in array2:
    if i in count:
        print(count[i], end=" ")
    else:
        print(0, end=" ")
 """


# 이분탐색
def bs(array, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if array[mid] == target:
        return count.get(target)
    elif array[mid] > target:
        return bs(array, target, start, mid - 1)
    else:
        return bs(array, target, mid + 1, end)


for i in array1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in array2:
    print(bs(array1, i, 0, len(array1) - 1), end=" ")
