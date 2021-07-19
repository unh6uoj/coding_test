def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    temp = ''
    for a in new_id:
        if a.isalpha() or a.isdigit() or a == '-' or a == '_' or a == '.':
            temp += a
    new_id = temp

    # 3단계
    while True:
        if new_id.find('..') == -1:
            break
        new_id = new_id.replace('..', '.')

    # 4단계, 5단계
    if new_id[0] == '.':
        new_id = new_id[1:]
    try:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    except:
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]

        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7단계
    if len(new_id) <= 2:
        while True:
            if len(new_id) == 3:
                break
            new_id += new_id[-1]

    answer = new_id

    return answer
