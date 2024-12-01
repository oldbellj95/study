# https://codeup.kr/problem.php?id=2001

p = list()
j = list()
for i in range(3):
    p.append(int(input()))
for i in range(2):
    j.append(int(input()))
print("%.1f" %((min(p) + min(j)) +  ((min(p) + min(j)) * 0.1)) )
