# input :       10
#               203 204 205 206 207 208 203 204 205 206
#               13
#               203 204 204 205 206 207 205 208 203 206 205 206 204
# ouput :       204 205 206
# explanation : As an example, the array with some numbers missing, arr=[7,2,5,3,5,3].
#               The original array of numbers brr=[7,2,5,4,6,3,5,3].
#               The numbers missing are [4,6]


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