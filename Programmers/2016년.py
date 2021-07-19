def solution(a, b):
    answer = ''

    month = {
        2: 31,
        3: 29,
        4: 31,
        5: 30,
        6: 31,
        7: 30,
        8: 31,
        9: 31,
        10: 30,
        11: 31,
        12: 30
    }

    weeks = {
        0: 'SUN',
        1: 'MON',
        2: 'TUE',
        3: 'WED',
        4: 'THU',
        5: 'FRI',
        6: 'SAT'
    }

    day = 0
    for i in range(2, a+1):
        day += month[i]
    day += b

    return weeks[(day-3) % 7]
