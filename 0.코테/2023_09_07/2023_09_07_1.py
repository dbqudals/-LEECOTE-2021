# 프로그래머스 해시 의상


def solution(clothes):
    answer = {}

    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1
    # print(answer.values())
    tmp = 1

    for i in list(answer.values()):
        tmp *= i + 1
    return tmp - 1
