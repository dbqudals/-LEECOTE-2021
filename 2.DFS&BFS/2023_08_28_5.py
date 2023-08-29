# DFS & BFS 기초문제(미로탈출)

""" 
입력예시: 5 6
101010
111111
000001
111111
111111

출력예시:
10

시작칸과 마지막칸도 세기
최소값 구하기 = BFS
"""

from collections import deque

n, m = map(int, input().split())
grpah = []

for _ in range(n):
    grpah.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if grpah[nx][ny] == 0:
                continue

            if grpah[nx][ny] == 1:
                grpah[nx][ny] = grpah[x][y] + 1
                queue.append((nx, ny))

    return grpah[n - 1][m - 1]


print(bfs(0, 0))
