function selectionSort (arr){
    for(let i = 0; i < arr.length - 1; i++){
        let minindex = i; 
        // minindex의 초기값을 0으로 해둬서 배열이 안됬었다.
        // 꼭. i로 지정해서 0이 아닌 탐색의 첫번째 인덱스가 초기값이 되게 해야한다.
        for(let j = i+1; j < arr.length; j++){
            if(arr[j] < arr[minindex]){
                minindex = j;
            }
        }
        let temp = arr[minindex];
        arr[minindex] = arr[i];
        console.log(temp, arr[minindex]);
        arr[i] = temp;
    }
    return arr;
}

let a = [43,12,53,11,25,63,22,19,32,771,627];
console.log(selectionSort(a));