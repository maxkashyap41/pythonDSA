def unitWater(arr, n):
    left = [-1]*n
    right = [-1]*n

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])
    
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])
    
    unit = 0
    for i in range(n):
        unit = unit+(min(left[i], right[i])-arr[i])
    
    return unit


if __name__ == "__main__":
    n = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    water = unitWater(arr, n)

    print("\nUnit of Water Stored-> ", water)
    print("\n")

    
