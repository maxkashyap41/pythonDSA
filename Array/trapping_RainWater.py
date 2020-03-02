# input       : 7,4,0,9
# output      : 10
# explanation : print the sum of those array blocks that stores the water. 


def trappingRainWater(arr, n):
    left = [-1]*n
    right = [-1]*n

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])
    print(left)
    
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])
    print(right)

    unit = 0
    for i in range(n):
        unit = unit+(min(left[i], right[i])-arr[i])
    
    return unit


if __name__ == "__main__":
    n = int(input("\nEnter the Number: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    
    unit = trappingRainWater(arr, n)
    
    print("\nTotal water stored: ", unit)
    print("\n")