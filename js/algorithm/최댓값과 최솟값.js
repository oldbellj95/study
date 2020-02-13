function solution(s) {
    var answer = ''; 
    let trim = s.split(' ');
    let max = Math.max.apply(null, trim);
    let min = Math.min.apply(null, trim);
    answer = min + ' ' + max;
    return answer;
}

