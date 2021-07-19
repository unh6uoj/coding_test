def solution(n):
    temp = ''
    a, b = divmod(n, 3)

    # 3진법 만들기
    while True:
        if a == 0:
            temp += str(b)
            break
        else:
            temp += str(b)

        a, b = divmod(a, 3)
    return int(temp, 3)
