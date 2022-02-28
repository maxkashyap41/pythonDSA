def pythagoreanTriplet(arr, n):
    squareArr = list(map(lambda i: i*i, arr))
    squareArr.sort()
    print(squareArr)

    for k in range(n-1, 1, -1):
        i = 0
        j = k-1
        while i <= j:
            sum = squareArr[i] + squareArr[j]
            if sum == squareArr[k]:
                return True
            elif sum < squareArr[k]:
                i += 1
            else:
                j -= 1
    
    return False



if __name__ == "__main__":
    print("\n")

    arr = [3,2,4,6,5]
    arr = [68,35,1,70,25,79,59,63,65,6,46,82,28,62,92,96,43,28,37,92,5,3,54,93,83,22,17,19,96,48,27,72,39,70,13,68,100,36,95,4,12,23,34,74]
    n = len(arr)

    # n = int(input("\nEnter the Number: "))
    # arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    if pythagoreanTriplet(arr, n) == True:
        print("YES !")
    else:
        print("NO")

    print("\n")