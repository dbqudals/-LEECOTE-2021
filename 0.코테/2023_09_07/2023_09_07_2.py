# 프로그래머스 스택/큐 프로세스

from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque(priorities)

    while queue:
        Max = max(queue)
        now = queue.popleft()
        location -= 1

        if Max != now:
            queue.append(now)

            if location < 0:
                location = len(queue) - 1
        else:
            answer += 1

            if location < 0:
                break

    return answer
