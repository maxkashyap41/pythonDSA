if __name__ == "__main__":
    arr = []
    n = int(input("\nEnter the Size of the Array Elements: "))
    print("Enter the Array Elements:")
    for i in range(n):
        a = int(input())
        arr.append(a)

    print("\nThe Array Elements are (in List form): ", arr)
    print("\nThe Array Elements are (in simple array form): ", end=" ")
    for i  in range(n):
        print(arr[i], end= " ")
    print()
    
    print("\n#######################################################################################################\n")

    m = int(input("Enter the Size of the Array Elements: "))
    array = list(map(int, input("\nEnter the Array Elements: ").strip().split()))[:m]

    print("\nThe Array Elements are (in List form): ", array)
    print("\nThe Array Elements are (in simple array form): ", end=" ")
    for i  in range(m):
        print(array[i], end= " ")
    print()
