# You are given an array of size N having no duplicate elements. The array can be categorized into following:
# 1.  Ascending
# 2.  Descending
# 3.  Descending Rotated
# 4.  Ascending Rotated
# Your task is to print which type of array it is and the maximum element of that array.


def typeArray(arr, n):
    sortArr = sorted(arr)

    maxN = max(arr)
    minN = min(arr)
    if maxN == arr[n-1] and minN == arr[0]:
        return maxN, 1
    elif maxN == arr[0] and minN == arr[n-1]:
        return maxN, 2
    else:
        if arr[0] == sortArr[-2]:
            return maxN, 3
        else:
            for i in range(n-1):
                if arr[i] == maxN:
                    if arr[i+1] == sortArr[-2]:
                        return maxN, 3
                    elif arr[i+1] == minN:
                        return maxN, 4


if __name__ == "__main__":
    print("\n")
    # arr = [2,1,5,4,3]         # arr = [5,4,3,2,1]
    # arr = [1,2,3,4,5]         # arr = [3,4,5,1,2]    
    arr = [766,455,428,422,358,189,182,897]
    n = len(arr)

    maxN, typeAr = typeArray(arr, n)
    print(maxN, typeAr)

    print("\n")