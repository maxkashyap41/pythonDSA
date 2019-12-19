def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    size = len(arr)
    print("\nLength of the Array ->", size, end=" ")

    print("\nElements are ->", end = " ")
    for i in range(size):
        print(arr[i], end = " ")

    bubble_sort(arr)
    
    print("\nSorted Array ->", end = " ")
    for i in range(size):
        print(arr[i], end = " ")
    print()