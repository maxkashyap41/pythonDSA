def CodeChef(arr, n):
    infectise = []
    count = 1
    i = 0
    while i < n-1:
        diff = arr[i+1]-arr[i]
        if diff <= 2:
            count = count+1
        else:
            infectise.append(count)
            count = 1
        i = i+1

    infectise.append(count)

    min_inf = min(infectise)
    max_inf = max(infectise)
    print(min_inf, max_inf)


if __name__ == "__main__":
    print("\n")
    # arr = [1,2,5,6,7]
    # arr = [3,6]
    # arr = [1,3,5]
    # arr = [1,2,5,6,7,8,12]
    t = int(input("\nEnter the TestCases: "))
    while t:
        n = int(input("\nEnter the size of the array: "))
        arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

        CodeChef(arr, n)
        
        print("\n")
        t = t-1
    
    print("\n")