def bubble_sort(arr, n):
    count = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                count = count+1
    
    return arr, count


if __name__ == "__main__":
    n = int(input("\nEnter the Number: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    res, c = bubble_sort(arr, n)
    print("\nSorted Array: ", end = " ")
    for i in range(n):
        print(res[i], end = " ")
    print("\nNumber of Swaps: ", c)
    print("\n")
