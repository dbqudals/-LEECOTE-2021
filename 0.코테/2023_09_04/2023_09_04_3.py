# 프로그래머스 완전탐색 모의고사
def solution(answers):
    math_1 = [1, 2, 3, 4, 5]
    math_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    answer = []

    for idx, val in enumerate(answers):
        if math_1[idx % 5] == val:
            score[0] += 1
        if math_2[idx % 8] == val:
            score[1] += 1
        if math_3[idx % 10] == val:
            score[2] += 1

    for i in range(len(score)):
        if max(score) == score[i]:
            answer.append(i + 1)

    return answer
