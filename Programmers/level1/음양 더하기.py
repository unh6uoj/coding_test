def solution(absolutes, signs):
    answer = 0
    
    for ab, si in zip(absolutes, signs):
        if si == False:
            ab *= -1
        answer += ab
        
    return answer