def miniSwaps(arr, n):
    temp = [-1]*(n+1)

    # changing the arr values as temp indecies and arr indecies as temp values
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos = pos+1
    
    count = 0
    for i in range(n):
        if arr[i] != i+1:
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
            count = count+1
    
    return arr, count


if __name__ == "__main__":
    n = int(input("\nEnter the Array Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    res, c = miniSwaps(arr, n)
    print("\nSorted Array: ", end = " ")
    for i in range(n):
        print(res[i], end = " ")
    print("\nMinimum Swaps done were", c)
    print("\n")
    
