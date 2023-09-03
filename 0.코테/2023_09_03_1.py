# 프로그래머스 해쉬 완주하지 못한 선수
def solution(participant, completion):
    count = {}
    Hashsum = 0

    for i in participant:
        count[hash(i)] = i
        Hashsum += hash(i)

    for j in completion:
        Hashsum -= hash(j)

    return count[Hashsum]
