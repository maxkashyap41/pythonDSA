def pythagoreanTriplet(arr, n):
    for i in range(n):
        arr[i] = arr[i] * arr[i]
    
    arr.sort()
    print(arr)

    for i in range(n-1, 1, -1):
        j = 0
        k = i-1
        while j < k:
            if arr[j]+arr[k] == arr[i]:
                return True
            else:
                if arr[j]+arr[k] < arr[i]:
                    j = j+1
                else:
                    k = k-1
    
    return False



if __name__ == "__main__":
    n = int(input("\nEnter the Number: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    if pythagoreanTriplet(arr, n) == True:
        print("YES !")
    else:
        print("NO")

    print("\n")