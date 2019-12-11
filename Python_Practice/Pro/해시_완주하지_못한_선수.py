import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

#그만 컨닝좀하자 
#새로운 거 알아낸건 좋은데 습득을 해야하지 않겠니..

