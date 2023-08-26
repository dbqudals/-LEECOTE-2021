result = 1000 - int(input())
moneys = [500, 100, 50, 10, 5, 1]
count = 0

for coin in moneys:
    count += result // coin
    result %= coin
print(count)
