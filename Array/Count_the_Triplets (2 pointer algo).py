def countTriplets(arr, n):
    arr.sort()

    count = 0
    



if __name__ == "__main__":
    # arr = [1,5,3,2]
    # arr = [3,2,7]
    # arr = [7,2,5,4,3,6,1,9,10,12]
    t = int(input("\nEnter the Number of Testcases: "))

    while t:
        n = int(input("Enter the Size of Array: "))
        arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

        ans = countTriplets(arr, n)
        print(ans if ans > 0 else -1)

        t = t-1

    print("\n")