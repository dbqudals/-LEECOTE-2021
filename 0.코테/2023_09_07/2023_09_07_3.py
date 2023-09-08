# 프로그래머스 완전탐색 카펫


def solution(brown, yellow):
    answer = []

    total = brown + yellow

    for b in range(1, total + 1):
        if (total / b) % 1 == 0:
            a = total / b

            if a >= b:
                if 2 * a + 2 * b - 4 == brown:
                    return [a, b]
    return answer
