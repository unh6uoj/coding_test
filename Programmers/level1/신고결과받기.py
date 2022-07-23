def solution(id_list, report, k):
    report_results = {id:[] for id in id_list}
        
    report = list(set(report))
    for item in report:
        user, target = item.split(" ")
        report_results[target].append(user)
    else:
        answer = {id:0 for id in id_list}
        for id in id_list:
            if len(report_results[id]) >= k:
                for user in report_results[id]:
                    answer[user] += 1
    
    
    return list(answer.values())