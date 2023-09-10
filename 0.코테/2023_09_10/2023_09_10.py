# 백준 2447


def Star(n):
    if n == 1:
        return ["*"]

    draw_star = Star(n // 3)
    result = []

    for i in draw_star:
        result.append(i * 3)

    for j in draw_star:
        result.append(j + " " * (n // 3) + j)

    for k in draw_star:
        result.append(k * 3)
    return result


n = int(input())

print("\n".join(Star(n)))
