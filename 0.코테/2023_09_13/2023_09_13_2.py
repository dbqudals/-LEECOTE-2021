# 백준 3040
answer = []

for i in range(9):
    answer.append(int(input()))

for i in range(9):
    for j in range(i + 1, 9):
        if sum(answer) - answer[i] - answer[j] == 100:
            x, y = i, j
            break

answer.pop(x)
answer.pop(y - 1)

for i in answer:
    print(i)
