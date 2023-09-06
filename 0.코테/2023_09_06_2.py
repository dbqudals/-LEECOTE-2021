# 프로그래머스 완전탐색 소수찾기

from itertools import permutations


def Prime_num(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def solution(numbers):
    answer = 0
    array = list(numbers)
    per = set()

    for i in range(1, len(numbers) + 1):
        result = list(permutations(array, i))

        for j in result:
            num = int("".join(j))
            per.add(num)

    for k in per:
        if Prime_num(k):
            answer += 1
    return answer
