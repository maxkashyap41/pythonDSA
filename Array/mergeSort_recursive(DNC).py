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
        k =k+1
    
    # for leftover elements in the array list
    while i <= up1:
        temp[k] = arr[i]
        i = i+1
        k = k+1
    while j <= up2:
        temp[k] = arr[j]
        j = j+1
        k = k+1


def sort(arr, temp, low, up):
    if low == up:
        return
    
    mid = (low+up) // 2
    sort(arr, temp, low, mid)
    sort(arr, temp, mid+1, up)

    merge(arr, temp, low, mid, mid+1, up)

    # copying temp to arr
    for i in range(low, up+1):
        arr[i] = temp[i]


def mergesort(arr, n):
    temp = [None for _ in range(n)]
    sort(arr, temp, 0, n-1)



if __name__ == "__main__":
    n = int(input("\nEnter the Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    mergesort(arr, n)

    print("\nSorted Array Elements are: ", end = " ")
    for i in range(n):
        print(arr[i], end = " ")
    
    print("\n")