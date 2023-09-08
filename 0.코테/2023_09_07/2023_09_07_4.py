# 프로그래머스 DFS/BFS 단어변환


from collections import deque


def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]
    answer = 0
    queue = deque()
    queue.append((begin, 0))

    while queue:
        now_val, now_idx = queue.popleft()

        if now_val == target:
            answer = now_idx
            break

        for i in range(len(words)):
            tmp = 0
            if not visited[i]:
                for j in range(len(now_val)):
                    if now_val[j] != words[i][j]:
                        tmp += 1
                if tmp == 1:
                    queue.append((words[i], now_idx + 1))
                    visited[i] = 1
    return answer
