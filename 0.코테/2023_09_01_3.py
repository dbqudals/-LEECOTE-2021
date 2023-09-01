# 백준 10799
""" 
'(' 일때는 stack
')' 일때는 제일 위가 '('이면 POP하고 현재까지 길이를 더하고
                    ')'이면 POP하고 1씩 더하기
"""

array = list(input())
answer = []
result = 0

for i in range(len(array)):
    if array[i] == "(":
        answer.append("(")
    else:
        if array[i - 1] == "(":
            answer.pop()
            result += len(answer)
        else:
            answer.pop()
            result += 1

print(result)
