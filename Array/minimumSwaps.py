def minSwap(arr, n):
    temp = [None]*(n+1)
    for pos, value in enumerate(arr):
        temp[value] = pos
        pos = pos+1
    
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
    n = int(input("\nEnter the Array Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    res = minSwap(arr, n)
    print("Minimum Number of Swaps are: ", res)
    print("\n")
