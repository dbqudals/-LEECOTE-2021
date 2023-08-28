# BFS 구현

from collections import deque


def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()
        print(now, end=" ")

        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * len(graph)

print(bfs(graph, 1, visited))
