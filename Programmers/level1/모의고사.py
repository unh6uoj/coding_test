def solution(answers):
    answer = []

    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score1 = 0
    score2 = 0
    score3 = 0

    index1 = 0
    index2 = 0
    index3 = 0

    for number in answers:
        if number == supo1[index1]:
            score1 += 1
        if number == supo2[index2]:
            score2 += 1
        if number == supo3[index3]:
            score3 += 1

        index1 += 1
        index2 += 1
        index3 += 1

        if index1 >= len(supo1):
            index1 = 0
        if index2 >= len(supo2):
            index2 = 0
        if index3 >= len(supo3):
            index3 = 0

    scores = [score1, score2, score3]

    maxScore = max(scores)

    for index, score in enumerate(scores):
        print(score)
        if score == maxScore:
            answer.append(index+1)

    return answer
