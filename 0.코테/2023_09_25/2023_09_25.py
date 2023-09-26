from collections import deque
import copy

N, M = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        now_x, now_y = queue.popleft()

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    global answer
    count = 0

    for i in range(N):
        count += tmp_graph[i].count(0)
    answer = max(answer, count)


def make_wall(count):
    if count == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count + 1)
                graph[i][j] = 0


answer = 0
make_wall(0)
print(answer)
