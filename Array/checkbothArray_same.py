def sameArray(arr, n):
    maxArr = [None]*n
    maxArr[0] = arr[0]
    for i in range(1, n):
        maxArr[i] = max(maxArr[i-1], arr[i])
    
    print(maxArr)

    if arr == maxArr:
        print("TRUE.")
    else:
        print("FALSE.")


if __name__ == "__main__":
    print("\n")

    # arr = [4, 3, 2, 7, 8, 9]
    # arr = [11, 9, 12]
    # arr = [12, 7, 10, 3, 9]
    # arr = [12, 7, 21, 24, 29]
    # arr = [4, 2, 5, 7]
    # arr = [7, 13, 10, 2, 3, 8, 11, 12, 17, 18, 19, 20]
    arr = [3, 10, 10]
    n = len(arr)

    sameArray(arr, n)

    print("\n")