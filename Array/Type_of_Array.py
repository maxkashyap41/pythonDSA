# You are given an array of size N having no duplicate elements. The array can be categorized into following:
# 1.  Ascending
# 2.  Descending
# 3.  Descending Rotated
# 4.  Ascending Rotated
# Your task is to print which type of array it is and the maximum element of that array.

def func(arr, n):
    sArr = sorted(arr)
    print(sArr)
    maxElement = sArr[n-1]
    minElement = sArr[0]
    if sArr == arr:
        return maxElement, 1
    elif sArr[::-1] == arr:
        return maxElement, 2
    else:
        for i in range(n-1):
            # arr[1] == maxElement has to be considered 
            # becoz of tc arr-[1,6,5,4].
            if arr[0] == maxElement or arr[1] == maxElement or arr[0] == minElement:
                if sArr[i] == arr[2]:
                    if sArr[i] < sArr[i+1] and arr[2] < arr[3]:
                        return maxElement, 4
                    else:
                        return maxElement, 3
            else:
                if sArr[i] == arr[0]:
                    if sArr[i] < sArr[i+1] and arr[0] < arr[1]:
                        return maxElement, 4
                    else:
                        return maxElement, 3


if __name__ == "__main__":
    print("\n")
    # arr = [2,1,5,4,3]
    arr = [5,4,3,2,1]
    # arr = [1,2,3,4,5]
    # arr = [3,4,5,1,2]    
    # arr = [766,455,428,422,358,189,182,897]
    # arr = [2,1,4,3,6,5]
    # arr = [3,4,5,6,1,2]
    # arr = [6,5,2,1,4,3]
    arr = [6,7,2,3]
    # arr = [1,6,5,4]
    n = len(arr)

    maxN, typeAr = func(arr, n)
    print(maxN, typeAr)

    print("\n")