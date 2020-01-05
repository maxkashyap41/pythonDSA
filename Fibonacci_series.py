def fibo(a, b, size):
    i = 0
    while i < size:
        print(a, end = " ")
        c = a+b
        a = b
        b = c
        i = i+1
    print("\n")


if __name__ == "__main__":
    size = int(input("\nSize please -> "))

    num1 = int(input("\nEnter the First Number: "))
    num2 = int(input("\nEnter the Second Number: "))
    print("\nFibonacci Series is: ", end = " ")
    fibo(num1, num2, size)

