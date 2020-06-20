def countTriplets(arr, n):
    arr.sort()
    arr_set = set(arr)
    maxN = arr[-1]
    Sum = 0
    count = 0
    for i in range(n-1):
        for j in range(i+1, n-1):
            Sum = arr[i]+arr[j]
            if Sum > maxN:
                break
            if Sum in arr_set:
                count = count+1
    
    return count



if __name__ == "__main__":
    # arr = [1,5,3,2]
    # arr = [3,2,7]
    # arr = [7,2,5,4,3,6,1,9,10,12]
    t = int(input("\nEnter the Number of Testcases: "))

    while t:
        n = int(input("Enter the Size of Array: "))
        arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

        ans = countTriplets(arr, n)
        print(ans if ans > 0 else -1)

        t = t-1

    print("\n")