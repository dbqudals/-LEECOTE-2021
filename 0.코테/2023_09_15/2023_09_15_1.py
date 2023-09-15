# 인프런 강의(DP)
""" cost = [10, 15, 20]


def dp(n):
    n = len(cost)
    memo = [-1] * (n + 1)
    memo[0] = 0
    memo[1] = 0

    for i in range(2, n + 1):
        memo[i] = min(memo[i - 2] + cost[i - 2], memo[i - 1] + cost[i - 1])
    return memo[n]


print(dp(len(cost) + 1))
 """


cost = [10, 15, 20]
memo = {}


def dfs(n):
    n = len(cost) + 1

    if n == 0 and n == 1:
        return 0

    if n not in memo:
        memo[n] = min(dfs(n - 1) + cost[n - 1], dfs(n - 2) + cost[n - 2])

    return memo[n]
