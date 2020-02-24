while True:
    i = input()
    if i == "-1":
        break
    else:
        result = 0
        a = list(map(int, i.split()))
        for index in range(len(a) - 1):
            if (a[index] * 2) in a:
                result += 1
        print(result)