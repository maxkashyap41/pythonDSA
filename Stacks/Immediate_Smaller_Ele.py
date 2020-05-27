def Immediate(arr, n):
    res = []
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            res.append(arr[i+1])
        else:
            res.append(-1)
    
    i = i+1
    if i == n-1:
        res.append(-1)
    
    return res




if __name__ == "__main__":
    print("\n")

    # arr = [4,2,1,5,3]
    # arr = [5,6,2,3,1,7]
    n = int(input("\nEnter the Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    ans = Immediate(arr, n)
    print("\nImmediate Smallest Elements corresponding to Right Side: ", end = '')
    for i in ans:
        print(i, end = ' ')

    print("\n")
