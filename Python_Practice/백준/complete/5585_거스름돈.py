c = 1000- int(input())
result = 0
coinlist = [500,100,50,10,5,1]
for index in coinlist:
    result += c // index
    c %= index
print(result)