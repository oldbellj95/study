let a = [6,3,2,1,7,5]
l = a.length

for(let i = 0; i < l; i++){
    let minindex = i;
    for(let j = i+1; j < l; j++){
        if(a[j] < a[minindex]){
            minindex = j
        }
        [a[i], a[minindex]] = [a[minindex], a[i]] 
    }
    console.log(a)
}