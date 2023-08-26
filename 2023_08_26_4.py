# 모험가 길드: 문제
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 그룹참여
# 최댓값

N = int(input())
scared = list(map(int, input().split()))
scared.sort()
# print(scared)
count = 0
g_count = 0

for i in scared:
    count += 1
    if count >= i:
        g_count += 1
        count = 0
print(g_count)
