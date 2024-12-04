function solution(n) {
    let answer = 0;
    // 주어진 n값의 값을 i에 넣는다. i에 값은 반복할때마다 1씩 감소한다. i 값이 0이되면 실행중단.
    for(let i = n; i > 0; i--){
        // 나머지연산으로 값이 떨어지면 answer의 나눠지는 약수의 값을 더해준다.
        if((n%i) == 0){
            answer += i
        }
    }
    return answer;
}