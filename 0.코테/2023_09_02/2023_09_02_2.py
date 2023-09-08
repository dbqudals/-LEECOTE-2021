# 프로그래머스 스택/큐 같은숫자는 싫어
def solution(arr):
    stack = []
    N = len(arr)

    for i in range(N - 1):
        if arr[i] != arr[i + 1]:
            stack.append(arr[i])
    stack.append(arr[-1])

    return stack
