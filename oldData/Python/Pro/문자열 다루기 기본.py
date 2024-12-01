def solution(s):
    return s.isdigit() and (len(s) == 4) or (len(s) == 6) 


# print( '1234'.isdigit() )
# # True
# print( '123edsd'.isdigit() )
# # False

# 이런식으로 문자열이 숫자로만 구성되면 참 문자가 섞이면 거짓으로 출력해준다.
# 문제의 출력 조건은 문자열의 길이가 4이거나 6인경우 문자열이 숫자로만 구성되있으면 참 아니면 거짓을 출력해야한다