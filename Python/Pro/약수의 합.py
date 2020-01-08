# 약수의 합
# 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 제한 사항
# n은 0 이상 3000이하인 정수입니다.

def solution(n):
    answer = 0
    for i in range(n+1):
        if i == 0:
            continue
        if n % i == 0:
            answer += i
    return answer

# 약수는 해당값으로 나눴을떄 0으로 떨어진다
# 0부터 n까지 1씩 올리면서 딱 나누어 떨어지면 결과값에 더해서 출력한다