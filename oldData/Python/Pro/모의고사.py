def solution(answers):
    answer = []
    r = [0,0,0]
    s1 = range(1, 6)
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]:
            r[0] += 1
        if answers[i] == s2[i % len(s2)]:
            r[1] += 1
        if answers[i] == s3[i % len(s3)]:
            r[2] +=1
    
    maxs = max(r)
    for i in range(len(r)):
        if r[i] >= maxs:
            answer.append(i + 1)
    return answer

# 완전 탐색 문제. 단순하게 생각하자.!

# 이걸 해답보고 푸는 바보도 얼마 없을거다

# 정답을 맞추는 학생의 답은 이미 제공 되어있으니까 그걸 리스트에 넣어서 반복해서 확인만 해주면된다
# 9,11,13번 줄처럼 현재 비교하려는 값과 학생이 제출한 정답을 비교하면 완전탐색으로 비교할수있다.