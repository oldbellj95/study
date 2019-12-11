/**7번 Reverse Integer
 * https://leetcode.com/problems/reverse-integer/
 * 숫자가 입력되면 역으로 출력한다
 * 32-bit signed integer 로 출력 되어야한다.
 * 범위를 벗어날경우 0을 출력한다

 * @param {number} x
 * @return {number}
*/ 
var reverse = function(x) {
    var result = 0;
    if(Math.sign(x) === -1){
        // Math.sign(input) 입력된 값의 부호를 출력한다
        // 출력값은 1, -1, 0, -1, NaN
        var a = String(x).split("").reverse().join("");
        /**
         * String(input) 입력된 값을 문자열로 출력한다.
         * split(분리할 기준, 분리할 개수) 
         * reverse() 뒤집는 함수
         * join(합칠 기준) 기준을 이용해 배열을 합쳐 문자열로 만든다
         */
        result = parseInt(a) * Math.sign(x);
        // parseInt(target) 입력된 값을 정수형으로 반환
    }else{
        result =  String(x).split("").reverse().join("");
    }    
    if(result < Math.pow(2, 31) -1 && result > Math.pow(2, 31) * -1){
        // Math.pow(base, exponext) 함수는 base를 exponent번 곱한 결과, base의 exponext제곱을 반환한다.
        // 32-bit signed integer의 범위안에 reverse한 결과값이 있을경우 출력한다 아닐경우 0 출력
        return result;
    }else{
        return 0;
    }
};