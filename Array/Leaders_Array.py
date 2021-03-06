def leadersArray(arr, n):
    leaders = [None]
    leaders[0] = arr[n-1]
    
    i = n-1
    while i > -1:
        j = i-1
        while j > -1 and arr[j] < arr[i]:
            j = j-1
        if j == -1:
            break
        else:
            leaders.append(arr[j])
            i = j

    leaders.reverse()
    print(leaders)


if __name__ == "__main__":
    print("\n")
    # arr = [16, 17, 4, 3, 5, 2, 7]
    # arr = [16, 17, 4, 3, 5, 2]
    # arr = [1, 2, 3, 4, 0]
    arr = [7, 4, 5, 7, 3]
    n = len(arr)

    leadersArray(arr, n)
    
    print("\n")