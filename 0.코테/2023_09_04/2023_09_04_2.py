# 프로그래머스 정렬 가장큰 수


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = ""

    for i in numbers:
        answer += i

    return str(int(answer))
