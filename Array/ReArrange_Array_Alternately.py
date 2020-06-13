def ReArrange_Array(arr, n):
    z = arr[n-1] + 1
    max_I = n-1
    min_I = 0

    for i in range(n):
        if i % 2 == 0:
            arr[i] = arr[i] + ((arr[max_I] % z) * z)
            max_I = max_I-1
        
        if i % 2 != 0:
            arr[i] = arr[i] + ((arr[min_I] % z) * z)
            min_I = min_I+1
    
    for i in range(n):
        arr[i] = arr[i] // z
    
    return arr


if __name__ == "__main__":
    # arr = [1,2,3,4,5,6]
    # n = len(arr)

    t = int(input("\nEnter the Testcases: "))
    
    while t:
        n = int(input("\nEnter the Array Size: "))
        arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

        res = ReArrange_Array(arr, n)
        print("After ReArrangement of the Array: ")
        for i in range(n):
            print(res[i], end = " ")

        print()
        t = t-1

    print("\n")