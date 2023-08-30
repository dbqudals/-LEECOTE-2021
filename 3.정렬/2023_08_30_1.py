# 두 배열의 원소 교체: 문제 설명
""" 
입력예시:
5 3
1 2 5 4 3
5 5 6 6 5

출력예시:
26
"""

n, k = map(int, input().split())

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

array1.sort()
array2.sort(reverse=True)

for i in range(k):
    if array1[i] < array2[i]:
        array1[i], array2[i] = array2[i], array1[i]

print(sum(array1))
