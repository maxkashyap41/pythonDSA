def MininmumSwaps(arr):
    


if __name__ == "__main__":
    num = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("\nEnter the Array Elements: ").strip().split()))[:num]
    # arr = [1, 5, 4, 3, 2]
    num = len(arr)
    swaps = MininmumSwaps(arr)
    print("Minimum Swaps are: ", swaps)
    print("\nArray Elements: ")
    for i in range(num):
        print(arr[i], end =" ")
    print("\n")