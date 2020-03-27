function solution(h) {
    var t = h.length;
    var answer = new Array(t);
    for(var q = 0; q < t; q++){
        answer[q] = 0;
    }
    for(var i = 0; i < h.lengths; i++){
        for(var j = 0; j < h.lengths - i; j++){
            if( h[h.lengths - i] < h[h.lengths-j]){
                answer[i] = h.lengths - j;
            }
            answer[i] = 0;
        }
    }
    return answer;
}

// 제일 끝 인덱스 부터 시작한다.
// 송신하는 탑보다 높은 탑이 있으면 그탑을 저장배열에 저장한다.
// 높은탑이 없으면 0을 저장배열에 저장한다