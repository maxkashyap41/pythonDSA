def frequency(arr, n):
    visited_arr = [False for _ in range(n)]

    for i in range(n):
        if visited_arr[i] == True:
            continue

        count = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                visited_arr[j] = True
                count = count+1
        
        print(arr[i], ":", count)

if __name__ == "__main__":
    n = int(input("\nEnter the Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    print("Frequency of Array of Elements: ")
    frequency(arr, n)
    print("\n")