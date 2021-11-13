def reverse(arr, n):
    mid = n // 2
    j = n-1
    for i in range(mid):
        arr[i], arr[j] = arr[j], arr[i]
        j -= 1
    
    print(arr)

if __name__ == "__main__":
    print("\n")
    # arr = [5, 4, 10, 12, 1]
    arr = [7, 9, 2, 99]
    n = len(arr)

    reverse(arr, n)
    print("\n")