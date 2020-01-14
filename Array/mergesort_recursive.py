def merge_sort(arr):
    n = len(arr)
    temp = [None]*n
    sort(arr, temp, 0, n-1)

def sort(arr, temp, low, up):
    if low == up:
        return
    
    mid = (low+up)//2
    sort(arr, temp, low, mid)
    sort(arr, temp, mid+1, up)

    merge(arr, temp, low, mid, mid+1, up)

    # copying temp to origin array
    for i  in range(low, up+1):
        arr[i] = temp[i]

def merge(arr, temp, low1, up1, low2, up2):
    i = low1
    j = low2
    k = low1

    while i <= up1 and j <= up2:
        if arr[i] > arr[j]:
            temp[k] = arr[j]
            j = j+1
        else:
            temp[k] = arr[i]
            i = i+1
        k = k+1
    
    while i <= up1:
        temp[k] = arr[i]
        i = i+1
        k = k+1
    while j <= up2:
        temp[k] = arr[j]
        j = j+1
        k = k+1


if __name__ == "__main__":
    arr = [35, 25, 10, 16, 56, 45, 34, 23, 12]
    n = len(arr)

    print("\nArray Elements are: ", end = " ")
    for i in range(n):
        print(arr[i], end = " ")

    merge_sort(arr)

    print("\nSorted Array Elements are: ", end = " ")
    for i in range(n):
        print(arr[i], end = " ")
    
    print("\n")
    
