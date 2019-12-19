def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

if __name__ == "__main__":
    arr = [4, 3, 2, 10, 12, 1, 5, 6]
    print("\nThe Array Elements are ->", end=" ")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    
    insertion_sort(arr)

    print("\nThe Sorted Array Elements are ->", end=" ")
    for i in range(len(arr)):
        print(arr[i], end=" ",)
    
    print()
