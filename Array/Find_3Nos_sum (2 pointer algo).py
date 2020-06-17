def triplet(arr, n, Sum):
    arr.sort()
    
    for i in range(0, n-2):
        l = i+1
        r = n-1
        while l < r:
            if arr[i]+arr[l]+arr[r] == Sum:
                return 1
            elif arr[i]+arr[l]+arr[r] < Sum:
                l = l+1
            else:
                r = r-1
    
    return 0


if __name__ == "__main__":
    print("\n")
    # arr = [1,4,45,6,10,8]
    # Sum = 13
    # arr = [1,2,4,3,6]
    # Sum = 10

    n, Sum = map(int, input("\nEnter the Size and Sum: ").split())
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    res = triplet(arr, n, Sum)
    print("Number of Combinations that consist: ", res)

    print("\n")