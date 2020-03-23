function mergeSort (arr){
    if (arr.length < 2) return arr;
    const center = arr.length + 1 /2;
    const al = arr.slice(0, center-1);
    const ar = arr.slice(center-1, arr[-1]);
    return merge(mergeSort(al), mergeSort(ar));
}
function merge(al, ar){
    let r = [];
    while(al.length && ar.length){
        if(al[0] >= ar[0]){
            r.push(ar.shift()); //shift 함수 배열의 첫번째 요소를 제거한뒤 리턴한다.
        }else{
            r.push(al.shift());
        }
    }
    while(al.length){r.push(al.shift());}
    while(ar.length){r.push(ar.shift());}
    return r;
}
const a = [43,12,53,11,25,63,22,19,32,771,627]
console.log(mergeSort(a));

// 배열을 받는다
// 받은 배열을 반으로 나눈다
// 나눈배열을 다시 합병정렬로 재귀시킨다
// 재귀시킨 배열의 길이가 1일때 
// 합병정렬로 합친다.