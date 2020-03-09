# input       : 1 2 3 4 5 6 7 8 10
#               
# output      : 9
# explanation : using the n natural numbers like n*(n+1)/2
#               
#   

def missingNumbers(arr, n):
    m = n+1
    sum_natural = m*(m+1) // 2

    sum_array = 0
    for i in range(n):
        sum_array = sum_array+arr[i]
    
    number = sum_natural-sum_array
    
    return number


if __name__ == "__main__":
    # print("\n")
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    # n = len(arr)

    n = int(input("\nEnter the Size of the Array: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

    number = missingNumbers(arr, n)

    print("Missing Number is: ", number)
    print("\n")
