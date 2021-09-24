def solution(n):
    answer = 0

    for a in range(1, n+1):
        if (pow(a, 2)) == n:
            return pow(a+1, 2)
    else:
        return -1
