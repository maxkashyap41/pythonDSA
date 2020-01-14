def selection_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min = j
        
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
        count = count+1
    return count

if __name__ == "__main__":
    #arr = [64, 25, 12, 22, 11]
    arr = [24, 11, 25, 26, 64]
    print("\nLength of the Array ->", len(arr), end=" ")

    print("\nThe Array Elements are ->", end=" ")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    
    swap = selection_sort(arr)

    print("\nThe Number of Swaps are: ", swap)

    print("\nThe Sorted Array Elements are ->", end=" ")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    
    print()
