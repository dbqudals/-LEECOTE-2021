# 문자열 재정렬
""" 
입력예시: K1KA5CB7
출력예시: ACBKK13

문자만 따로 붙이기 join으로 나머지는 정렬
*isalpha() -> 일파벳 판별
"""

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print("".join(result))
