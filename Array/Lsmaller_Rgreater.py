def middleElement(arr, n):
    leftArr = [None]*n
    leftArr[0] = leftArr[n-1] = False
    maxL = arr[0]
    for i in range(1, n-1):
        if maxL <= arr[i]:
            maxL = arr[i]
            leftArr[i] = True
        else:
            leftArr[i] = False
    
    print(leftArr)

    rightArr = [None]*n
    rightArr[0] = rightArr[n-1] = False
    minR = arr[n-1]
    for i in range(n-2, 0, -1):
        if minR >= arr[i]:
            minR = arr[i]
            rightArr[i] = True
        else:
            rightArr[i] = False
    
    print(rightArr)

    for i in range(n):
        if leftArr[i] == True and rightArr[i] == True:
            return arr[i]
    
    return -1



if __name__ == "__main__":
    print("\n")

    # arr = [4, 3, 2, 7, 8, 9]
    # arr = [11, 9, 12]
    # arr = [12, 7, 10, 3, 9]
    # arr = [12, 7, 21, 24, 29]
    # arr = [4, 2, 5, 7]
    # arr = [7, 13, 10, 2, 3, 8, 11, 12, 17, 18, 19, 20]
    # arr = [3, 10, 10]
    # arr = [7, 10, 14, 15, 5, 16]
    arr = [2, 3, 9, 1, 3]
    n = len(arr)

    # middleElement(arr, n)
    element = middleElement(arr, n)
    print("Found Element is: ", element)

    print("\n")
