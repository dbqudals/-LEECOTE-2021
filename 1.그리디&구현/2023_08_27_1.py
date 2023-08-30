# 시각: 문제설명
"""
모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 구하시오
입력예시: 5(N)
출력예시: 11475

00시 00분 00초 ~ N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우
시각 문제는 3중 포문으로 해결 할 수 있다
완전탐색 문제 -> 하루는 어차피 86400초이니까
"""

N = int(input())
count = 0
for hour in range(N + 1):
    for min in range(60):
        for sec in range(60):
            if "3" in str(hour) + str(min) + str(sec):
                count += 1

print(count)
