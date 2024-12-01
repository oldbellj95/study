def solution(prices):
    answer = []
    l = []
    index = len(prices)
    for i in range(index):
        temp = prices.pop()
        count = 0
        for j in range(len(l) -1, -1, -1):
            if temp <= l[j]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
        l.append(temp)
    answer.reverse()
    return answer

p = [1, 2, 3, 2, 3]
print(solution(p))
print("예상 출력값 : [4, 3, 1, 1, 0]")