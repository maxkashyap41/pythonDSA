def LeetCode(arr, n):
    maxNo = arr[0]
    for i in range(n):
        if maxNo < arr[i]:
            maxNo = arr[i]
    
    hasht = [0]*(maxNo+1)
    for i in range(n):
        hasht[arr[i]] = hasht[arr[i]]+1
    
    print(hasht)

    i = 0 # representing hasht
    j = 0 # representing arr
    count = 0
    while j < n:
        if arr[j]+1 == i:
            if hasht[i] != 0:
                count = count+1
                j = j+1
                i = 0
            else:
                j = j+1
                i = 0
        else:
            if arr[j]+1 <= maxNo:
                i = i+1
            else:
                j = j+1
                i = 0
    
    return count


if __name__ == "__main__":
    print("\n")
    # arr = [1,3,2,3,5,0]
    # arr = [1,2,3]
    # arr = [1,1,3,3,5,5,7,7]
    arr = [1,1,2,2]
    n = len(arr)
    print("Array Elements are: ", end = " ")
    for i in range(n):
        print(arr[i], end = " ")
    print("\n")

    res = LeetCode(arr, n)
    print(res)
    print("\n")