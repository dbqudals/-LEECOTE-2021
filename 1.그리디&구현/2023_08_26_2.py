# 1이 될 때까지

""" 
1. N에서 1을 뺀다.
2. N을 K로 나눕니다.
"""

n, k = map(int, input().split())
count = 0

while True:
    # 나누어 떨어지는 수가 나올 때 까지 빼기
    # 몫 연산자
    target = (n // k) * k
    count += n - target
    n = target

    if n < k:
        break

    count += 1
    n //= k

# 남은 수에서 1일 될때까지 빼는 수를 더함
count += n - 1
print(count)
