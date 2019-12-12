n = int(input())
inputlist = []
for i in range(0,n):
    inputlist.append(int(input()))

inputlist.sort()
for i in range(0,n):
    print(inputlist[i])