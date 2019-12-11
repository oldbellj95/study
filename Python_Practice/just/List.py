
#리스트 List
list_a = [1,2,3,4,5,5,6,7,87,8,9,9,6,6,34]
print(type(list_a))
print(list_a[0])

#리스트는 여러타입이 혼합 포함될수 있음
list_b = ["abc", 294, False]
print(list_b)

#리스트 선언
list_c = []
print(type(list_c))
list_d = list()
print(type(list_d))

#인덱스는 0부터 시작함
print(list_a[0])

#리스트에 요소 추가
print("add to list")
list_a.append(38372) #원소 마지막에 추가
print("add last index")
print(list_a)
print("\n")

list_a.insert(0,12312) # insert(삽입할 index, 값)
print("using insert (0,12312)")
print(list_a)
print("\n")


list_c = list_a + list_b  #+를 이용한 추가 
print("using +")
print(list_c)
print("\n")


list_a.extend([1,6,2]) # extend를 이용한 추가
print("using extend")
print(list_a)
print("\n")


#리스트 원소 삭제
print("delete is list")
del list_a[0]
print("using del keyword")
print(list_a)
print("\n")


# 정렬. .sort는 기본적으로 오름차순 적용 
a = [1,2,3,4,5,6,7,8,9,10]
a.reverse()
print("reverse (just reverse it)")
print(a)

a = [1,7,4,3,6,4,76,2,3,4,2]
a.sort()
print("sort (usally sort work Ascending)")
print(a)

a = [45,1,56,67,5,7,45,62,35,235,]
a.sort(reverse=True) #내림차순 사용시
print("sort (using reverse=True it work Dscending)")
print(a)
a.sort()
print(a)


