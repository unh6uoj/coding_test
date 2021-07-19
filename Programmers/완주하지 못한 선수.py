def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        try:
            if participant[i] == completion[i]:
                continue
            else:
                return participant[i]
        except:
            return participant[-1]
