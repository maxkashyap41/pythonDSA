def LargestSmallest(arr, n):
    sort_arr = sorted(arr)
    length = len(sort_arr)
    mid = length // 2
    res = [-1]*n
    
    # for largest
    x = 0
    for i in range(n-1, mid-1, -1):
        res[x] = sort_arr[i]
        x = x+2

    # for smallest
    x = 1
    for i in range(0, mid, 1):
        res[x] = sort_arr[i]
        x = x+2
    
    return res


if __name__ == "__main__":
    # print("\n")
    # arr = [5, 10, 15, 2, 3, 9, 7, 8, 11]
    # n = len(arr)
    # LargestSmallest(arr, n)
    # print("\n")

    n = int(input("\nEnter the Array Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    res = LargestSmallest(arr, n)
    print("\nSorted List: ", end = " ")
    for i in range(len(res)):
        print(res[i], end = " ")
    print("\n")


