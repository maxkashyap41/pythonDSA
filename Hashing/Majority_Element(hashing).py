def majority(arr, n):
    maxNo = arr[0]
    for i in range(n):
        if maxNo < arr[i]:
            maxNo = arr[i]
    
    hashT = [0]*(maxNo+1)
    for i in range(n):
        hashT[arr[i]] = hashT[arr[i]]+1
    
    print(hashT)

    hashMaxNo = hashT[0]
    for i in range(len(hashT)):
        if hashMaxNo < hashT[i]:
            hashMaxNo = hashT[i]
            element = i
    
    # for i in range(len(hashT)):
    #     if hashMaxNo == hashT[i]:
    #         element = i
    
    print(element)
    
    nBy2 = n // 2
    if hashMaxNo > nBy2:
        return element
    else:
        return -1


if __name__ == "__main__":
    print("\n")
    # arr = [3, 1, 3, 3, 2]
    arr = [1, 2, 3]
    # arr = [2, 2, 2, 2, 1, 1]
    n = len(arr)

    number = majority(arr, n)
    print("Majority Element: ", number)

    print("\n")
