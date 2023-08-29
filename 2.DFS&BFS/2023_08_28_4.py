# DFS & BFS 기초문제(얼음)

""" 
입력예시: 4 5
00110
00011
11111
00000

출력예시: 3 
"""


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False


n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
