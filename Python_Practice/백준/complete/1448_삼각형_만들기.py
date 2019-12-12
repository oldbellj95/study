import sys
input = sys.stdin.readline
n = int(input())
inputlist = []
result = -1
for index in range(n):
    inputlist.append(int(input())) 
inputlist.sort(reverse = True)
for index in range(0,n-2):
    a,b,c = inputlist[index],inputlist[index + 1], inputlist[index + 2]
    if a < (b + c):
        result = a + b + c
        break
print(result)