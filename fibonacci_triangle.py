def fib_TriAngle(a, b, size):
    i = 1
    while i <= size:
        #print(, end = " ")
        j = 1
        while j <= i:
            c = a+b
            print(a, end = " ")
            a = b
            b = c
            j = j+1
        print("\n")
        i = i+1


if __name__ == "__main__":
    size = int(input("\nEnter the Size: "))
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print("\n")
    fib_TriAngle(a, b, size)
    print("\n")

