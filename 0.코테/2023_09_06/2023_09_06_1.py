# 프로그래머스 정렬 H-Index
def solution(citations):
    citations.sort(reverse=True)

    for idx, val in enumerate(citations):
        if idx >= val:
            return idx
    return len(citations)
