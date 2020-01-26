def missingNumbers(arr, n):
    visited_a = [False for i in range(n)]
    
    for i in range(n):
        if visited_a[i] == True:
            continue

        countA = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                visited_a[j] = True
                countA = countA+1
        print(arr[i], countA)


if __name__ == "__main__":
    arr = [3, 4, 5, 6, 7, 8, 3, 4, 5, 6]
    n = len(arr)
    print("\n")
    missingNumbers(arr, n)
    print("\n")