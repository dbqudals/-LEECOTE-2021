# 프로그래머스 DFS/BFS 네트워크
def solution(n, computers):
    answer = 0

    def dfs(x):
        visited[x] = True

        for i in range(n):
            if not visited[i] and computers[x][i]:
                dfs(i)

    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer
