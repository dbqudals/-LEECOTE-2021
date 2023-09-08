# 백준 1439
""" 
입력:
0001100

출력: 1

주어진 숫자가 모두 1이 되거나 0이 되는 최소한의 수를 구하여라
풀이: 숫자가 변할때를 카운팅 한다음 +1 // 2을 통해 구한다.
"""

numbers = input()
count = 0

for i in range(len(numbers) - 1):
    if numbers[i] != numbers[i + 1]:
        count += 1

print((count + 1) // 2)
