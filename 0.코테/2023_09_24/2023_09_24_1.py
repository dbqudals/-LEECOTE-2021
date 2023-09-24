from collections import deque

M, N = map(int, input().split())
graph = []
count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
for _ in range(N):
    graph.append(list(map(int, input().split())))


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

# print(x, y)


def bfs():
    while queue:
        now_x, now_y = queue.popleft()

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[now_x][now_y] + 1


bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    count = max(count, max(i))

print(count - 1)
