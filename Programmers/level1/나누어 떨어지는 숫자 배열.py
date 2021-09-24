def solution(arr, divisor):
    answer = []

    for ele in arr:
        if ele % divisor == 0:
            answer.append(ele)

    answer.sort()

    try:
        print(answer[0])
    except:
        answer.append(-1)

    return answer
