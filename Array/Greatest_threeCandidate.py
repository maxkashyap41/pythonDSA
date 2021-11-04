def greatest3(arr, n):
    arr.sort();
    return max(arr[n-1] * arr[n-2] * arr[n-3], arr[0] * arr[1] * arr[n-1]);


if __name__ == "__main__":
    n = int(input("\nEnter the Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    ans = greatest3(arr, n)
    print("Product is: ", ans)
    print("\n")