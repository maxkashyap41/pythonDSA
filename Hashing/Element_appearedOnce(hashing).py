def elementOnce(arr, n):
    maxNo = arr[0]
    for i in range(n):
        if maxNo < arr[i]:
            maxNo = arr[i]
    
    hashT = [0]*(maxNo+1)

    for i in range(n):
        hashT[arr[i]] = hashT[arr[i]]+1
    
    # print(hashT)

    for i in range(len(hashT)):
        if hashT[i] == 1:
            return i



if __name__ == "__main__":
    print("\n")
    arr = [1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65]
    n = len(arr)

    element = elementOnce(arr, n)
    print("Element that appeared once:~ ", element)
    print("\n")