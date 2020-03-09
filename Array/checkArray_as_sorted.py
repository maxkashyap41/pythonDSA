def checkArray(arr, n):
    i = 1
    while i < n-1:
        if arr[i] < arr[i+1] and arr[i] > arr[i-1] or arr[i] > arr[i+1] and arr[i] < arr[i-1]:
            i = i+1
        else:
            return False
    
    return True

    
if __name__ == "__main__":
    print("\n")
    # arr = [13, 2, 15, 6, 4]
    # arr = [2, 4, 6, 13, 15]
    # arr = [2, 4, 6, 8, 5, 3, 1]
    arr = [8, 5, 3, 4]
    n = len(arr)
    if checkArray(arr, n):
        print("It's a Sorted Array !")
    else:
        print("It's an UnSorted Array !")
    
    print("\n")

        