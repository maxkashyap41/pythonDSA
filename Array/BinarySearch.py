def binarySearch(arr, n, value):
    pos = -1
    low = 0
    up = n-1
    while low <= up:
        mid = (low+up) // 2
        if arr[mid] == value:
            pos = mid
            break
        else:
            if arr[mid] < value:
                low = mid+1
            else:
                up = mid-1
    
    if pos != -1:
        print("\nValue Found at position", (pos+1))
    else:
        print("\nValue not Found !")


if __name__ == "__main__":
    # print("\n")
    # value = 22
    # arr = [4, 7, 8, 12, 45, 99, 102]
    # n = len(arr)
    # binarySearch(arr, n, value)
    # print("\n")
    n = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    value = int(input("Enter the value that you wanna seacrh: "))

    arr.sort()
    binarySearch(arr, n, value)

    print("\n")
