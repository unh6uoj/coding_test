def solution(a, b):
    answer = 0
    for ele_a, ele_b in zip(a, b):
        answer += ele_a * ele_b
    return answer
