# 백준 15649
""" from itertools import permutations

N, M = map(int, input().split())
answer = []

for i in range(1, N + 1):
    answer.append(i)

result = list(permutations(answer, M))

for i in result:
    print(" ".join(map(str, i))) """


# 2번 풀이(백트래킹,DFS)

N, M = map(int, input().split())
result = []


def dfs():
    if len(result) == M:
        print(" ".join(map(str, result)))

    for i in range(1, N + 1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()


dfs()
