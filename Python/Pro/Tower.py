def solution(heights):
    answer = [0] * len(heights)
    while heights:
        right = heights.pop()
        for index in range(len(heights) - 1 , -1 , -1):
            if right < heights[index]:
                answer[len(heights)] = index + 1
                break
    return answer