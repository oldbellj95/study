def solution(p):
    p.sort()
    for i in range(1,len(p)):
        if p[0] in p[i]:
            return False
    return True

# 처음에 정렬을 안하고 문제를 풀일해서 일부분제가 풀리지않고 효율성테스트도 다 떨어졌었다.
# 처음에 정렬를 하고 진행하니 적은 숫자부터 문제를 풀게되서 그런지 잘됬다..
# 괜히 찾아본듯.. 정럴한번 돌려보고 하면될걸;;