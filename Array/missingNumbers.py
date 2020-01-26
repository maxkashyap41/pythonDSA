def missingNumbers(arr, brr):
    m = len(arr)
    n = len(brr)
    maxno = brr[0] 
    for i in range(1, n):
        if brr[i] > maxno:
            maxno = brr[i]
    # print("\nMaxNo: ",maxno)

    hash1 = [0]*(maxno+1)
    hash2 = [0]*(maxno+1)

    for i in range(m):
        hash1[arr[i]] = hash1[arr[i]]+1
    for i in range(n):
        hash2[brr[i]] = hash2[brr[i]]+1
    
    res = []
    for i in range(maxno+1):
        if hash1[i] == 0 and hash2[i] == 0:
            continue
        elif hash2[i] > hash1[i]:
            res.append(i)
    print(res)


        

if __name__ == "__main__":
    arr = [3, 4, 5, 6, 7, 8, 3, 4, 5, 6]
    brr = [3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 3, 4, 5]
    missingNumbers(arr, brr)