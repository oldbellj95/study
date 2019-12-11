#버블 정렬
#시간복잡도는 O(n²) 공간복잡도 O(n)
def bubbleSort(list):
    for loop_count in range(len(list)-1,0,-1):
        for index in range(loop_count):
            if list[index] > list[index+1]:
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp
    return list


#선택정렬
#시간복잡도 O(n²)
#가장 큰수를 찾아서 배열의 마지막위치와 교환함.

def selectionSort(list):
    for offset in range(0, len(list) - 1):
        offset_minvalue = offset
        for num in range(offset+1, len(list)):
            if list[num] < list[offset_minvalue]:
                offset_minvalue = list[num]
            temp = list[offset_minvalue]
            list[offset_minvalue] = list[offset]
            list[pffset] = temp
    return list

#삽입정렬 
#현재위치보다 아래쪽을 순회하며 알맞은 위치에 값을 넣는 정렬
#시간복잡도 O(n) 
def insertionSort(list):
    for i in range(1, len(list)):
        currentvalue = list[i]
        position = index

        while position>0 and list[position - 1] > currentvalue:
            list[position] = list[position - 1]
            position -= 1
        list[position] = currentvalue
        return list


#병합 정렬
# merge Sort
# 반으로 계속 나누고 그 리스트 안에서 정렬한뒤 병합해서 다시 정렬함.
# 시간복잡도 O(nlogn)

def mergeSort(list):
    if len(list) <=1:
        return list
    mid = len(list) // 2
    leftlist = list[:mid]
    rightlist = list[mid:]
    L = mergeSort(leftlist)
    R = mergeSort(rightlist)
    i , j = 0
    result = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1

    result += L[i:]
    result += R[j:]
    return result



#퀵정렬
#불안정 정렬, 
# 피벗을 선정한다음 피벗을 기준으로 오른쪽 왼쪽으로 나눈다.
# 


     