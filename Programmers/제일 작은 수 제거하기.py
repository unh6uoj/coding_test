def solution(arr):
    del arr[arr.index(min(arr))]
    return [-1] if len(arr) == 0 else arr
