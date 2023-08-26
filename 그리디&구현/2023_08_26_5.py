# 상하좌우
""" 입력 예시
    5
    RRRUDD
    
    출력 예시
    3 4
"""

n = int(input())
plans = input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

LRUD = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(len(LRUD)):
        if plan == LRUD[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
