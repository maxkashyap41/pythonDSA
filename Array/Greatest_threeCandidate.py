def greatest3(arr, n):
    new_A = sorted(arr)
    p1 = new_A[n-1]*new_A[n-2]*new_A[n-3]
    p2 = new_A[0]*new_A[1]*new_A[n-1]

    res = max(p1, p2)
    return res


if __name__ == "__main__":
    n = int(input("\nEnter the Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    ans = greatest3(arr, n)
    print("Product is: ", ans)
    print("\n")