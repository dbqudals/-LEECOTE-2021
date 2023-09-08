# 프로그래머스 해시_전화번호 목록


def solution(phone_book):
    count = {}

    for i in phone_book:
        count[i] = 1

    for j in phone_book:
        result = ""

        for k in j:
            result += k

            if result in count and result != j:
                return False
    return True
