
# 입력
# 첫째 줄 입력 사람의 수 N
# 둘째 줄 입력 각 사람이 돈을 인출하는데 걸리는 시간 

# 각사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는
# 프로그램

# 그리디 알고리즘.

# 1번쨰 사람 자기 자신의 출력 시간
# 두번째 사람 1의 시간 + 자기 시간
# 세번쨰 사람 그전까지의 시간 + 자기시간

# 예제 

# 5
# 3 1 4 3 2
# 32


n = int(input())
tl = list(map(int, input().split()))
tl.sort()
obj = 0
wait = 0
for i in range(0, n):
    if i == 0:
        obj = obj + tl[i]
        wait = wait + tl[i]
    else:
        obj = obj + tl[i] + wait
        wait = wait + tl[i]
print(obj)


# 다른사람의 풀이

n = int(input())
num = list(map(int, input().split()))
num.sort()
t = [0]*n
for i in range(n):
    t[i] = t[i - 1] + num[i]
print(sum(t))
