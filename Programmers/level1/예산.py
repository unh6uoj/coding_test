def solution(d, budget):
    answer = 0

    d.sort()

    for n in d:
        budget -= n
        if budget == 0:
            answer += 1
            break
        elif budget > 0:
            answer += 1
            continue
        elif budget < 0:
            budget += n
            continue

        print(budget)

    return answer
