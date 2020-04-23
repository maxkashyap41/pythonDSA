def LeetCode(arr, n):
    xor = arr[0]
    for i in range(1, n):
        xor = xor^arr[i]
    
    return xor


if __name__ == "__main__":
    print("\n")
    # arr = [4, 1, 2, 1, 2]
    # arr= [2, 2, 1]
    arr = [3, 3, 6, 1, 2, 6, 2]
    n = len(arr)
    res = LeetCode(arr, n)
    print("Only Number in the Array: ", res)
    print("\n")