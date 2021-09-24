def solution(a, b):
    answer = 0

    big = max(a, b)
    small = min(a, b)

    for index in range(small, big+1):
        answer += index

    return answer
