def merge(arr, l, m, r):
        l_size = m-l+1
        r_size = r-m
        
        leftArr = []
        rightArr = []
        
        for i in range(l_size):
            leftArr.append(arr[l+i])
        for j in range(r_size):
            rightArr.append(arr[m+1+j])
        
        print(leftArr, rightArr)
        
        i = j = 0
        k = l
        while i < l_size and j < r_size:
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k +=1
        
        # for leftover elements
        while i < l_size:
            arr[k] = leftArr[i]
            i += 1
            k += 1
        while j < r_size:
            arr[k] = rightArr[j]
            j += 1
            k += 1
        
        
def mergeSort(arr, l, r):
    if l < r:
        mid = (l+r) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)
        merge(arr, l, mid, r)



if __name__ == "__main__":
    n = int(input("\nEnter the Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    mergeSort(arr, 0, n-1)

    print("\nSorted Array Elements are: ", end = " ")
    for i in range(n):
        print(arr[i], end = " ")
    
    print("\n")