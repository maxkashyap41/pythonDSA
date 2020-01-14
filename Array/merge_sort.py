def merge_sort(arr):
    n = len(arr)

    if(n > 1):
        mid = n//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = R[j]
                j = j+1
            else:
                arr[k] = L[i]
                i = i+1
            
            k = k+1

        while i < len(L):
            arr[k] = L[i]
            i = i+1
            k = k+1
        while j < len(R):
            arr[k] = R[j]
            j = j+1
            k = k+1


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82]

    size = len(arr)
    print("\nLength of the Array ->", size, end=" ")

    print("\nThe Array Elements are ->", end=" ")
    for i in range(size):
        print(arr[i], end=" ")

    merge_sort(arr)

    print("\nThe Sorted Array Elements are ->", end=" ")
    for i in range(size):
        print(arr[i], end = " ")
        
    print("\n")