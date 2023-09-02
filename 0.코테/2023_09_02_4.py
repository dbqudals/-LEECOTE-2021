# 프로그래머스 정렬 K번째 수
def solution(array, commands):
    result = []
    new_array = []
    for i, j, k in commands:
        for nums in range(i - 1, j):
            new_array.append(array[nums])
        new_array.sort()
        result.append(new_array[k - 1])
        new_array = []
    return result
