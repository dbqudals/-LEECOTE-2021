# 백준 1789

s = int(input())
total = 0
count = 0

for i in range(1, s + 1):
    total += i
    count += 1

    if total == 2:
        print(1)
        break

    if total == s:
        print(count)
        break

    elif total > s:
        print(count - 1)
        break
