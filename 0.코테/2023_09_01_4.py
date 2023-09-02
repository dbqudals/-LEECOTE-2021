# 백준 1992
""" 
쿼드 트리

입력:
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
"""
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]


def dfs(x, y, n):
    check = graph[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end="")
        n //= 2
        dfs(x, y, n)
        dfs(x, y + n, n)
        dfs(x + n, y, n)
        dfs(x + n, y + n, n)
        print(")", end="")

    elif check == 1:
        print(1, end="")
    else:
        print(0, end="")


dfs(0, 0, n)
