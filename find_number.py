def findnum(arr, k):
    n = len(arr)
    flag = -1

    for i in range(n):
        if arr[i] == k:
            flag = i
            break
    
    if flag == -1:
        print("\nNo !")
    else:
        print("\nYes !")

if __name__ == "__main__":
    n = int(input("\nEnter the size of the Number: "))
    arr = list(map(int, input("Enter the Array Elements: ").strip().split()))[:n]
    #arr = [1, 2, 3, 4, 5]
    print("\nElements are: ", arr) 
    k = 12
    findnum(arr, k)