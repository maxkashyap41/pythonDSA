# **    According to study made the k depends on the brr row size and 
#       the j depends on the brr col size and i depends on the row size of arr.
#
# **    The resultant matrix will depend on the col size of the brr.
#
# **    if arr row size == brr row size than only matrix will be possible
#       and if arr row size != brr row size than no matrix is formed !



def MatrixMul(arr, brr, a, a1, b, b1):
    res = []
    for i in range(a):
        res.append([])
        for j in range(b1):
            res[i].append(j)
            res[i][j] = 0
    
    if a == b:
        for i in range(a):
            for j in range(b1):
                Sum = 0
                for k in range(b):
                    Sum = Sum+arr[i][k]*brr[k][j]
                res[i][j] = Sum
        return res
    else:
        return -1



if __name__ == "__main__":
    print("\n")

    # arr = [
    #     [2,4],
    #     [6,8]
    # ]

    # brr = [
    #     [7,5],
    #     [3,1]
    # ]

    # arr = [
    #     [2,4],
    #     [6,8]
    # ]

    # brr = [
    #     [3],
    #     [8]
    # ]

    arr = [
        [2,4],
        [6,8],
        [7,9]
    ]

    brr = [
        [7,5],
        [3,1]
    ]

    a = len(arr)
    for i in range(a):
        a1 = len(arr[i])
    
    b = len(brr)
    for i in range(b):
        b1 = len(brr[i])

    ans = MatrixMul(arr, brr, a, a1, b, b1)
    if ans == -1:
        print("\nMatrix not possible !")
    else:
        print(ans)

    print("\n")