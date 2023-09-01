# 백준 9012
n = int(input())

for i in range(n):
    stack = []
    array = input()

    for j in array:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break

    else:
        if not stack:
            print("YES")
        else:
            print("NO")
