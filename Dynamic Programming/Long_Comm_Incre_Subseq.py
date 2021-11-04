def LongIncreCS(arr, n, brr, m):
    temp = [0 for k in range(m)]

    for i in range(n):
        count = 0
        for j in range(m):
            if arr[i] == brr[j]:
                if count+1 > temp[j]:
                    temp[j] = count+1
            
            if arr[i] > brr[j]:
                if temp[j] > count:
                    count = temp[j]
    
    ans = max(temp)
    return ans

if __name__ == "__main__":
    print("\n")

    arr = [3,4,9,1]
    brr = [5,3,8,9,10,2,1]
    # arr = [1,1,4,3]
    # brr = [1,1,3,4]

    n = len(arr)
    m = len(brr)

    res = LongIncreCS(arr, n, brr, m)
    print(res)

    print("\n")