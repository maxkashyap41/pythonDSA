def equibPoint(arr, n):
    right_sum = 0
    for i in range(1, n):
        right_sum = right_sum+arr[i]
    
    left_sum = 0
    for i in range(n):
        right_sum = right_sum-arr[i+1]
        left_sum = left_sum+arr[i]
        if left_sum == right_sum:
            return arr[i+1]


if __name__ == "__main__":
    n = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    ele = equibPoint(arr, n)
    print("Equilibrium Element: ", ele)
    print("\n")
    
