def LeetCode(arr, n):
    left = [0]*n
    left[0] = 1
    for i in range(1, n):
        left[i] = left[i-1]*arr[i-1]
    
    right = [0]*n
    right[n-1] = 1
    for i in range(n-2, -1, -1):
        right[i] = right[i+1]*arr[i+1]
    
    for i in range(n):
        left[i] = left[i]*right[i]
    
    del right
    print(left)


if __name__ == "__main__":
    print("\n")
    arr = [1, 2, 3, 4]
    # arr = [5, 3, 10, 4]
    n = len(arr)
    LeetCode(arr, n)
    print("\n")

