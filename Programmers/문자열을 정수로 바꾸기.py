def solution(s):
    return int(s) if s.find('-') == -1 else int(s[1:]) * -1
