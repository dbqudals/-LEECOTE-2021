# 인프런 강의(DP)


def Unique_path(m, n):
    graph = [[-1] * n for _ in range(m)]

    def dp(r, c):
        unique_path = 0
        if r == 0 and c == 0:
            graph[r][c] = 1
            return graph[r][c]

        if graph[r][c] == -1:
            if r - 1 >= 0:
                unique_path += dp(r - 1, c)
            if c - 1 >= 0:
                unique_path += dp(r, c - 1)

            graph[r][c] = unique_path
        return graph[r][c]

    return dp(m - 1, n - 1)


print(Unique_path(3, 7))
