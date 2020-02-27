def selectionSort(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
    
    return arr


if __name__ == "__main__":
    n = int(input("\nEnter the Array Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    res = selectionSort(arr, n)
    print("\nSorted Elements are: ", end = " ")
    for i in range(len(res)):
        print(res[i], end = " ")
    print("\n")
