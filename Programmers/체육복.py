def solution(n, lost, reserve):
    answer = 0

    # 사람 수 만큼 리스트 생성
    # 모든 학생이 1개의 체육복이 있다고 가정
    people = [1 for i in range(n)]

    # 도난당한 학생의 체육복 -1
    # 여분 학생의 체육복 +1
    for l in lost:
        people[l-1] -= 1
    for r in reserve:
        people[r-1] += 1

    print(people)

    for index, p in enumerate(people):
        if p == 0:
            if index != 0 and people[index-1] > 1:
                people[index-1] -= 1
                people[index] += 1
                answer += 1
            elif index != n-1 and people[index+1] > 1:
                people[index+1] -= 1
                people[index] += 1
                answer += 1
        else:
            answer += 1
    print(people)

    return answer
