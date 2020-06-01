def insertionSort(arr, n):
    for i in range(n):
        key = arr[i]
        j = i-1
        while j > -1 and key < arr[j]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j = j-1
    
    return arr


if __name__ == "__main__":
    n = int(input("\nEnter the Array Size: "))
    arr = list(map(int, input("Enter the Array Elements are: ").split()))[:n]
    sorted_arr = insertionSort(arr, n)
    print("\nSorted Elements are: ", end = " ")
    for i in range(len(sorted_arr)):
        print(sorted_arr[i], end = " ")
    print("\n")