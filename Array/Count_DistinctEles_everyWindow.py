def CountDistinct(arr, n, k):
    res = []
    maxN = max(arr)
    hashT = [0]*(maxN+1)

    dis_count = 0
    for i in range(0, k):
        if hashT[arr[i]] == 0:
            dis_count = dis_count+1
        
        hashT[arr[i]] = hashT[arr[i]]+1
    
    res.append(dis_count)

    for i in range(k, n):
        if hashT[arr[i-k]] == 1:
            dis_count = dis_count-1
        
        hashT[arr[i-k]] = hashT[arr[i-k]]-1
        
        if hashT[arr[i]] == 0:
            dis_count = dis_count+1
        
        hashT[arr[i]] = hashT[arr[i]]+1
        
        res.append(dis_count)
    
    return res




if __name__ == "__main__":
    print("\n")
    # arr = [1,2,1,3,4,2,3]
    # k = 4
    # arr = [4,1,1]
    # k = 2
    n, k = map(int, input("\nEnter the Size of the Array and K window: ").split())
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    ans = CountDistinct(arr, n, k)
    print("\nNumber of Distinct Elements in Every Window are:", ans)

    print("\n")