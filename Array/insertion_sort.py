def insertionSort(arr):
    size = len(arr)
    for i in range(1, size):
        j = i-1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp


if __name__ == "__main__":
    size = int(input("\nEnter the Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:size]
    
    insertionSort(arr)

    print("Sorted Array Elements are: ", end = " ")
    for i in range(size):
        print(arr[i], end = " ")
    print("\n")
