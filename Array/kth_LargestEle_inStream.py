def naiveApproach(arr, n, k):
    arr.sort()
    print(arr)
    print("\n")

    count = 1
    ptr = n-1
    i = n-1
    while i > -1:
        if count == k:
            arr[ptr] = arr[i]
            ptr = ptr-1
            i = ptr
            count = 1
        else:
            i = i-1
            count = count+1

    while ptr > -1:
        arr[ptr] = -1
        ptr = ptr-1

    print(arr)


if __name__ == "__main__":
    print("\n")
    arr = [1, 2, 3, 4, 5, 6]
    # arr = [3, 4]
    # arr = [1, 2, 3, 4, 5, 5, 6, 6, 6]

    n = len(arr)
    k = 47

    naiveApproach(arr, n, k)

    print("\n")