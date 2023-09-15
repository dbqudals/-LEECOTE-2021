# 백준 11651

n = int(input())

answer = []

for _ in range(n):
    answer.append(list(map(int, input().split())))

answer.sort(key=lambda x: (x[1], x[0]))

for i in answer:
    print(i[0], i[1])
