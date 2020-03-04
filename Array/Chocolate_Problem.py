def chocolateProb(arr, n, m):
    arr.sort()
    
    min_ = 99999999999
    i = 0
    j = m-1
    while j < n:
        res = arr[j]-arr[i]
        if min_ > res:
            min_ = res
        j = j+1
        i = i+1
    return min_
        

if __name__ == "__main__":
    # arr = [7, 3, 2, 4, 9, 12, 56]
    # n = len(arr)
    # m = 3
    n = int(input("\nEnter the Size of the Array: "))
    m = int(input("Enter the Number of Students: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    res = chocolateProb(arr, n, m)

    print(res)

    print("\n")