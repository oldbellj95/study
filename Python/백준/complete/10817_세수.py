# 10817 세수

# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

# 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)

# 두 번째로 큰 정수를 출력한다.

# 20 30 10
# 20
# 30 30 10
# 30

#단순하게 생각했다. 입력값을 받아서 정렬한뒤 가운데값을 출력했다. 야매인건가..
l = list(map(int, input().split()))
l.sort()
print(l[1])

#다른사람의 풀이. 나도 처음에 이런식으로 접근하려고 했었다.

a, b, c = map(int, input().split())
if a > b:
    if a > c :
        if b > c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if b > c:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        print(b)
