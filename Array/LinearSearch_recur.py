def linearSearch(arr, low, up, value):
    if low > up:
        return -1
    if arr[low] == value:
        return low
    elif arr[up] == value:
        return up
    
    return linearSearch(arr, low+1, up-1, value)


if __name__ == "__main__":
    # print("\n")
    # value = 4
    # arr = [5, 8, 4, 6, 9, 2]
    # n = len(arr)
    # binarySearch(arr, n, value)
    # print("\n")
    n = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    value = int(input("Enter the value that you wanna seacrh: "))

    pos = linearSearch(arr, 0, n-1, value)
    if pos != -1:
        print("\nValue Found at position", (pos+1))
    else:
        print("\nValue not Found !")

    print("\n")