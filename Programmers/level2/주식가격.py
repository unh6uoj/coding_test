def solution(prices):
    answer = []
    
    for index, price in enumerate(prices):
        count = -1
        for i in range(index, len(prices)):
            count += 1
            if price > prices[i]:
                answer.append(count)
                break
        else:
            answer.append(count)
    return answer