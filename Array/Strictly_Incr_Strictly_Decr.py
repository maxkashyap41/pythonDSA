# input: 1,2,3,4,5,4,3,2,1
# output: 5
# explain: before 5 every elements are increasing and after 5 every elements are decreasing.

def highest(arr, n):
    l = 0
    r = n-1
    while l < r:
        mid = (l+r) // 2
        if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
            return arr[mid]
        else:
            if arr[mid] < arr[mid+1]:
                l = mid+1
            else:
                r = mid-1
    
    if l == r:
        return arr[l]


if __name__ == "__main__":
    print("\n")
    # arr = [1,2,3,4,5,4,3,2]
    # arr = [1,2,3,4,5,6,5,4,3,2,1]
    arr = [1,2,3,4,5]
    n = len(arr)

    res = highest(arr, n)
    print(res)

    print("\n")
