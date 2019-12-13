a = [43,12,53,11,25,63]

for(let i =0; i < a.length; i ++){
    for(let j = 0; j < a.length; j++){
        if(a[j] > a[j+1]){
            [a[j], a[j+1]] = [a[j+1], a[j]]   
            // javascript는 swap함수가 따로 없고 그냥 값 넣어주는식으로 하면됨
        }
    }
}
console.log(a)