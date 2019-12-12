n = int(input())
s = list(input())
l = list(map(int, s))
result = 0
for i in range(n):
    result += l[i]
print(result)

#문자열을 하나씩 바로 자르고 싶으면 list(input()) 으로 입력받으면 됨