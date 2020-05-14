def LeetCode(arr, n):
    r = 0
    l = 0
    while r < n:
        if arr[r] == 0:
            r = r+1
        else:
            arr[r], arr[l] = arr[l], arr[r]
            l = l+1
            r = r+1
    
    return arr


if __name__ == "__main__":
    print("\n")
    arr = [0,1,0,3,12]
    n = len(arr)
    print("Array Elements are: ", arr)

    res = LeetCode(arr, n)
    print("\nResultant Array is: ", res)

    print("\n")