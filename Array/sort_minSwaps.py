def MininmumSwaps(arr):
    n = len(arr)
    temp = [None]*(n+1)
    for i, val in enumerate(arr):
        temp[val] = i
        i = i+1
    
    count = 0
    for i in range(n):
        if arr[i] != (i+1):
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
            count = count+1
    return count


if __name__ == "__main__":
    num = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("\nEnter the Array Elements: ").strip().split()))[:num]
    # arr = [1, 5, 4, 3, 2]
    num = len(arr)
    swaps = MininmumSwaps(arr)
    print("Minimum Swaps are: ", swaps)
    print("\nArray Elements: ")
    for i in range(num):
        print(arr[i], end =" ")
    print("\n")