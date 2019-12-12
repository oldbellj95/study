n, k = map(int, input().split())
coinlist= []
for i in range(n):
    coinlist.append(int(input()))

coinlist.sort(reverse=True)
count = 0

for i in range(n):
    t = coinlist[i]
    c = k//t
    if c != 0:
        count += c
        k -= t*c
print(count)


# 그리디 알고리즘
# 제발좀 컨닝좀 하지말자 정종헌아
