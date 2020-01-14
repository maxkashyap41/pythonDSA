def bubble_sort(arr, n):
    if(n == 1):
        return
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    
    bubble_sort(arr, n-1)

    
if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    size = len(arr)
    print("\nLength of the Array ->", size, end=" ")

    print("\nElements are ->", end = " ")
    for i in range(size):
        print(arr[i], end = " ")

    bubble_sort(arr, size)

    print("\nSorted Array ->", end = " ")
    for i in range(size):
        print(arr[i], end = " ")
        
    print()