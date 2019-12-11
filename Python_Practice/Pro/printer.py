def solution(array, commands):
    answer = []
    for index in range(len(commands)):
        newlist = []
        i, j, k = commands[index][0], commands[index][1], commands[index][2]
        newlist = array[i -1 : j]
        newlist.sort()
        answer.append(newlist[k - 1]) 
    return answer


