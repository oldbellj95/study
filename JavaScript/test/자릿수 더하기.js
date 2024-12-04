function solution(n)
{
    let answer = 0;
    // 받은 숫자값을 문자열로 변경
    let answerString = String(n);
    // 바꾼 문자열의 길이를 변수에 저장
    let stringLength = answerString.length;
    
    // 반복문. 들어온 값의 길이동안 반복.
    for(let i = stringLength; i > 0; i--){
        // 입력된 숫자값을 하나씩 answer변수에 더하기로 추가해줌.
        // 인덱스는 0부터 시작, substring 함수를 이용해서 1개씩 추출.
        answer += Number(answerString.substring(i-1, i));
    }
    return answer;
}