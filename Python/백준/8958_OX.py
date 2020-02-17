n = int(input())
for index in range(n):
    data = list(input())
    result = 0
    adder = 0
    for j in data:
        if j == 'O':
            adder += 1
        else:
            adder = 0
        result += adder
    print(result)
                 