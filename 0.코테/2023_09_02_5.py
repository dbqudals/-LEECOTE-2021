# 프로그래머스 정렬 최소직사각형
def solution(sizes):
    array2 = []
    array1 = []

    for i in sizes:
        array2.append(max(i))
        array1.append(min(i))

    return max(array2) * max(array1)
