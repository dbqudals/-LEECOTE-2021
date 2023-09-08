# 프로그래머스 DFS/BFS 게임 맵 최단거리

from collections import deque


def solution(maps):
    col = len(maps[0])
    row = len(maps)

    visited = [[-1] * col for _ in range(row)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        now_x, now_y = queue.popleft()

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if 0 <= nx < row and 0 <= ny < col:
                if visited[nx][ny] == -1 and maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[now_x][now_y] + 1
    return visited[row - 1][col - 1]

