def solution(s):
    answer = ''

    if len(s) % 2 == 0:  # 짝수
        answer += s[int(len(s)/2) - 1]
        answer += s[int(len(s)/2)]
    else:   # 홀수
        answer += s[int(len(s)/2)]

    return answer
