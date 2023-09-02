# 프로그래머스 해시 폰켓몬
def solution(nums):
    count = {}
    N = len(nums)
    result = 0

    for i in range(N):
        if nums[i] in count:
            count[nums[i]] += 1
        else:
            count[nums[i]] = 1

    for j in count:
        if j != j + 1:
            if result < N // 2:
                result += 1
    return result
