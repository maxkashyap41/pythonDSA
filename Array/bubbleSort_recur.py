def bubbleSort(arr, n):
    if n == 1:
        return
    count = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            count = count+1
    bubbleSort(arr, n-1)
    
    return arr, count


if __name__ == "__main__":
    n = int(input("\nEnter the Number: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    res, c = bubbleSort(arr, n)
    print("\nSorted Array: ", end = " ")
    for i in range(n):
        print(res[i], end = " ")
    print("\nNumber of Swaps: ", c)
    print("\n")