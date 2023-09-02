# 프로그래머스 DFS/BFS 타겟넘버
from collections import deque


def solution(numbers, target):
    n = len(numbers)
    queue = deque()
    answer = 0
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])

    while queue:
        now_val, now_idx = queue.popleft()
        now_idx += 1

        if now_idx < n:
            queue.append([now_val + numbers[now_idx], now_idx])
            queue.append([now_val - numbers[now_idx], now_idx])
        else:
            if now_val == target:
                answer += 1
    return answer
