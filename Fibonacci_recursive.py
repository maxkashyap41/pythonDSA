def Fib(size):
    if size == 0:
        return 0
    
    if size == 1:
        return 1
    
    return Fib(size-1) + Fib(size-2)


if __name__ == "__main__":
    n = int(input("\nEnter the index number for the Fibonacci Number: "))
    res = Fib(n)
    print("\nAt pos", n, "we get Fibonacci Number as", res)
    print("\n")
