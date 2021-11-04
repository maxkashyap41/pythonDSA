def Merge_invCount(arr, temp, low, mid, up):
    i = k = low
    j = mid+1
    count = 0
    while i <= mid and j <= up:
        if arr[i] > arr[j]:
            temp[k] = arr[j]
            count = count+(mid-i+1)
            j = j+1
        else:
            temp[k] = arr[i]
            i = i+1
        k = k+1
    
    while i <= mid:
        temp[k] = arr[i]
        i = i+1
        k = k+1
    
    while j <= up:
        temp[k] = arr[j]
        j = j+1
        k = k+1
    
    return count

def sort(arr, temp, low, up):
    count = 0

    if low < up:
        mid = (low+up) // 2

        count = count+sort(arr, temp, low, mid)
        count = count+sort(arr, temp, mid+1, up)

        count = count+Merge_invCount(arr, temp, low, mid, up)

        for i in range(low, up+1):
            arr[i] = temp[i]

    return count

def mergeSort(arr, n):
    temp = [0 for k in range(n)]

    count = sort(arr, temp, 0, n-1)
    return count


if __name__ == "__main__":
    print("\n")

    # arr = [2,4,1,3,5]
    arr = [8,7,6,3,2]
    n = len(arr)

    count = mergeSort(arr, n)
    print("Number of Inverses Present are:", count)

    print("\n")