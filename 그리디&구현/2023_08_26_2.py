n, k = map(int, input().split())

count = 0

while True:
    # 나누어 떨어질 수 있는 수 찾기
    target = (n // k) * k
    # 1 빼는 수 세기
    count += n - target

    n = target

    if n < k:
        break

    count += 1
    n //= k

count += n - 1

print(count)
