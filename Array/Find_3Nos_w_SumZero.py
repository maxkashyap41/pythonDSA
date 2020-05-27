def triplet(arr, n):
    for i in range(n-2):
        l = i+1
        r = n-1
        while l < r:
            Sum = arr[i]+arr[l]+arr[r]
            if Sum == 0:
                return 1
            elif Sum < 0:
                l = l+1
            else:
                r = r-1
    
    return 0


if __name__ == "__main__":
    print("\n")

    # arr = [0,-1,2,-3,1]
    # arr = [1,2,3]
    n = int(input("\nEnter the Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    ans = triplet(arr, n)
    print(ans)

    print("\n")