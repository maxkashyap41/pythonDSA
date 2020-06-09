def BooleanString(str1):
    arr = list(str1)
    n = len(arr)
    
    i = 0
    while i < (n-1):
        if arr[i] == 'A':
            x = int(arr[i-1]) * int(arr[i+1])
            arr[i+1] = str(x)
        
        if arr[i] == 'B':
            x = int(arr[i-1]) + int(arr[i+1])
            # boundary condition if 1B1 = 2 then
            if x == 2:
                x = x-1
            arr[i+1] = str(x)
        
        if arr[i] == 'C':
            x = int(arr[i-1]) ^ int(arr[i+1])
            arr[i+1] = str(x)

        i = i+1
    
    return arr[n-1]


if __name__ == "__main__":
    # str1 = '1C1B1B0A0'
    # str1 = '1A0B1'

    t = int(input("\nEnter the Number of Testcases: "))

    while t:
        str1 = str(input("Enter the String: "))
        ans = BooleanString(str1)
        print("The Resultant Answer is: ", ans)

        t = t-1

    print("\n")