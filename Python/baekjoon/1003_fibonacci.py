j = int(input())

zero = [1,0,1]
one = [0,1,1]

def fun(n):
    l = len(zero)
    if l <= n:
        for i in range(l,n + 1):
            zero.append(zero[n-1] + zero[n-2])
            one.append(one[n-1] + one[n-2])
    print("%d %d" %(zero[n], one[n]))

for j in range(j):
    a = int(input())
    fun(a)