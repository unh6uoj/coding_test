def solution(s):
    temp = [ord(i) for i in s]
    temp.sort()
    temp.reverse()

    return ''.join([chr(i) for i in temp])
