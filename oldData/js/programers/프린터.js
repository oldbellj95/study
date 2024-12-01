function solution(p, l) {
    let targetIndex = l;
    let a = 1;
    let first;
    while(p.length > 0){
        first = p.shift();
        if(p.some((value, index)=> value > first)){
            p.push(first);
        }
        else{
            if(targetIndex === 0){
                break;
            }
            else{
                a++;
            }
        }if(targetIndex ===0) targetIndex = p.length - 1;
        else targetIndex --;
    }
    return a;
}



console.log(solution([2, 1, 3, 2] , 2)); //return 1
console.log(solution([1, 1, 9, 1, 1, 1],0)); // return5