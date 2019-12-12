n = int(input())
inputlist = []
for i in range(0,n):
    inputlist.append(int(input()))



for i in range(0,n):
    print(inputlist[i])


def mergesort(a):
    if len(a) <= 1:
        return a
    
    left = mergesort(a[:len(a)/2])
    right = mergesort(a[len(a)/2:])

    
