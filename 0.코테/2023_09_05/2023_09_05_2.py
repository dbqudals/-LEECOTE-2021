# 프로그래머스 스택/큐 올바른 괄호


def solution(s):
    stack = []

    for i in s:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if stack:
                stack.pop()
            else:
                return False
                break

    if len(stack) == 0:
        return True
    return False
