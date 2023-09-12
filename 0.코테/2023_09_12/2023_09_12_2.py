# 인프런 강의


def two_sum(array, target):
    array.sort()

    i = 0
    n = len(array) - 1

    while i < n:
        if array[i] + array[n] > target:
            n -= 1

        elif array[i] + array[n] < target:
            i += 1
        else:
            return True
    return False


nums = [4, 1, 9, 7, 5, 3, 16]
target = 14

print(two_sum(nums, target))
