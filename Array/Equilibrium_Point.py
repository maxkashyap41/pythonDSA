def equibPoint(arr, n):
    right_sum = 0
    for i in range(n):
        right_sum = right_sum+arr[i]
    
    left_sum = 0
    j = 0
    for i in range(n):
        right_sum = right_sum-arr[i]
        left_sum = left_sum+arr[j]
        if (left_sum-arr[i]) == right_sum:
            return arr[i]
        j = j+1
    return None


if __name__ == "__main__":
    n = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    ele = equibPoint(arr, n)
    print("Equilibrium Element: ", ele)
    print("\n")
    
