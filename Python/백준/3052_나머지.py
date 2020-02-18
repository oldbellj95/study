l = list()
for i in range(10):
    l.append(int(input())%42)
l = set(l)
print(len(l))


# 파이썬에서 순서 상관없이 리스트의 중복을 제거해야할 경우 set이라는 함수를 사용하면 된다