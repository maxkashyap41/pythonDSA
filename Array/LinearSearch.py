def linearSearch(arr, n, value):
    pos = -1
    i = 0
    while i < n:
        if arr[i] == value:
            pos = i
            break
        i = i+1
    
    if pos != -1:
        print("\nValue Found at position", (pos+1))
    else:
        print("\nValue not Found !")


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

    linearSearch(arr, n, value)

    print("\n")