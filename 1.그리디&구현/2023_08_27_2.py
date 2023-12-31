# 왕실의 나이트
""" 
입력예시 : a1
출력예시 : 2
"""

input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord("a")) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 or next_column >= 1 or next_row <= 8 or next_column <= 8:
        result += 1

print(result)
