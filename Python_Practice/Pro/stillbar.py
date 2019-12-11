
def solution(arrangement):
    stack = []
    result = 0
    for i in range(len(arrangement)):
            if arrangement[i] == "(":
                stack.append(arrangement[i])
            else:
                stack.pop()
                if arrangement[i - 1] == "(":
                    result += len(stack)
                else:
                    result += 1
    return result

data = input()
print(solution(data))

