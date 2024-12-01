def solution(arr):
    s = 0
    for i in range(len(arr)):
        s += arr[i]
    return s / len(arr)

# 넘나 쉬운것. 