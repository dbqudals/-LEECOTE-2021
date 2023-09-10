# 백준 10101

result = []
for i in range(3):
    n = int(input())
    result.append(n)


if result.count(60) == 3:
    print("Equilateral")
elif sum(result) == 180 and len(set(result)) == 2:
    print("Isosceles")
elif sum(result) == 180 and len(set(result)) == 3:
    print("Scalene")
else:
    print("Error")
