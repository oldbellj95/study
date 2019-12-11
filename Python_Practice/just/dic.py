#딕셔너리
#관계형 자료형 (연관배열이라고 하기도함)

#선언 {key : value}
dic = {'첫번째' : 1, '두번째': 2 ,'세번째':3}
print(dic)

#딕셔너리에 쌍 추가하기 
dic[4] = 4
print(dic)

dic['다섯번째'] = 5
print(dic)

#삭제 del 키워드 이용
del dic[4]
print(dic)
print("\n")

print("딕셔너리의 키의 값만 구하기")
print(dic.keys()) 
print("\n")
print("딕셔너리의 value값만 구하기")
print(dic.values())
print("\n")
print("딕셔너리의 key, value 쌍으로 구하기")
print(dic.items())
print("\n")

print("딕셔너리 안의 모든 값을 삭제하기 dic.clear()")
dic.clear()
print(dic)
print("\n")

dic = {1:123123,2:1239912,3:281982}
print("key로 value 얻기 (get)")
print(dic.get(1))

dic['추가한것'] = '값입니다'
print(dic)

a = {'name' : '홍길동', 'birth':1128, 'age':30}
print(a)