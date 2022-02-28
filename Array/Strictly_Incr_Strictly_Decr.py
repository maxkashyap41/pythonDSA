# input: 1,2,3,4,5,4,3,2,1
# output: 5
# explain: before 5 every elements are increasing and after 5 every elements are decreasing.


def IncrDecr(arr, n):
    left = 0
    right = n-1
    
    while left < right:
        mid = (left + right) // 2
        if left == mid:
            print(arr[right])
            return arr[right]
        
        if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
            return arr[mid]
        else:
            if arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid-1
    
    if left == right:
        return arr[left]



if __name__ == "__main__":
    print("\n")
    # arr = [1,2,3,4,5,4,3,2]
    # arr = [1,2,3,4,5,6,5,4,3,2,1]
    arr = [1,2,3,4,5]
    n = len(arr)

    res = IncrDecr(arr, n)
    print(res)

    print("\n")
