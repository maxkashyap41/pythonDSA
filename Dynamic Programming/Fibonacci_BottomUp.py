def Fib(num):
    if num == 1 or num == 2:
        return 1
    arr = [None]*(num+1)
    arr[1] = 1
    arr[2] = 1
    for i in range(3, num+1):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[num]


if __name__ == "__main__":
    num = int(input("\nEnter the Number: "))
    result = Fib(num)
    print("Given Number Fibonacci Number is: ", result)
    print("\n")