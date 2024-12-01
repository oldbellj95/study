def solution(s):
    # answer = ""
    # for i in range(len(s)):
    #     answer += s[len(s)-1-i]
    return ''.join(sorted(s , reverse = True))

# sorted 함수를 사용하면 list.sort() 함수를 사용하는것 보다 편하게 가능한듯.
# sorted의 매개변수는 (list, key ,옵션)
# key랑 옵션을 넣지 안고 동작할경우 기본적으로 오름차순으로 동작함