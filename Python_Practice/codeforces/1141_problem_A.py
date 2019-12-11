n,m = map(int, input().split())
move = 0
if (m % n) == 0:
    m = m / n
    while m != 1:
        if (m % 3) == 0:
            m /= 3
            move += 1
        elif(m % 2) == 0:
            m /= 2
            move += 1
        else:
            move = -1
            break
else:
    move = -1
print(move) 