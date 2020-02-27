def binarySearch(arr, l, r, value):
    if l <= r:
        mid = (l+r) // 2
        if arr[mid] == value:
            pos = mid
            return pos
        else:
            if arr[mid] < value:
                return binarySearch(arr, mid+1, r, value)
            else:
                return binarySearch(arr, l, mid-1, value)
    else:
        return -1


if __name__ == "__main__":
    n = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    value = int(input("Enter the value that you wanna seacrh: "))

    arr.sort()
    pos = binarySearch(arr, 0, n-1, value)
    if pos != -1:
        print("\nValue Found at position", (pos+1))
    else:
        print("\nValue not Found !")

    print("\n")