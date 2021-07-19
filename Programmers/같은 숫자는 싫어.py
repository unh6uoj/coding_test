def solution(arr):
    answer = []

    answer.append(arr[0])
    for index in range(0, len(arr)):
        next = -1
        try:
            next = arr[index+1]
        except:
            pass

        if next != arr[index] and next != -1:
            answer.append(next)

    return answer
