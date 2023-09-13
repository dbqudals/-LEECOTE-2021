# 백준 11403
import sys

N = int(sys.stdin.readline().rstrip())

maps = []

for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if maps[i][k] and maps[k][j]:
                maps[i][j] = 1

for i in maps:
    print(" ".join(map(str, i)))
