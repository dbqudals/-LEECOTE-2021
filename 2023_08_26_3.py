# +,x 연산자를 넣어 만들어질 수 있는 가장 큰 수

numbers = input()

first = int(numbers[0])

for i in range(1, len(numbers)):
    num = int(numbers[i])

    if first == 0 or num == 0:
        first += num
    else:
        first *= num

print(first)
