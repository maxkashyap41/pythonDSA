def unitWater(arr, n):
    unit = 0
    for i in range(n):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
        
        right = arr[i]
        for j in range(i+1, n-1):
            right = max(right, arr[j])
        
        unit = unit+(min(left, right)-arr[i])
    
    return unit



if __name__ == "__main__":
    n = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    water = unitWater(arr, n)

    print("\nUNit of Water Stored-> ", water)
    print("\n")