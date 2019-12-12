a, b = map(int, input().split())
count = 0


Matrix = [[0]*a for i in range(b)]

for j in range(a):
    wb = list(input())
    for k in range(b):
        Matrix[j][k] = wb
    


