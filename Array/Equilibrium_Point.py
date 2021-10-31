def equibPoint(arr, n):
    Sum = 0
    for i in range(n):
        Sum = Sum + arr[i]

    curr_sum = 0
    for j in range(n):
        Sum = Sum - arr[i]
        curr_sum = curr_sum + arr[i]
        if (curr_sum-arr[i]) == Sum:
            return arr[i]

    return None


if __name__ == "__main__":
    n = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    ele = equibPoint(arr, n)
    print("Equilibrium Element: ", ele)
    print("\n")
    
