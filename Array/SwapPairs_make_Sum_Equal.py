def SwapPairsArray(arr, a, brr, b):
    pass


if __name__ == "__main__":
    print("\n")

    # arr = [4,1,2,1,1,2]
    # brr = [3,6,3,3]
    arr = [5,7,4,6]
    brr = [1,2,3,8]
    a = len(arr)
    b = len(brr)
    
    # a, b = map(int, input("\nEnter the Size of the Arrays: ").split())
    # arr = list(map(int, input("Array Elements: ").split()))[:a]
    # brr = list(map(int, input("Brray Elements: ").split()))[:b]

    ans = SwapPairsArray(arr, a, brr, b)
    print("\nBoth the Array has pair or not ", ans)

    print("\n")
