def GCD(x, y):
    if(y == 0):
        return x
    else:
        return GCD(y, x%y)

if __name__ == "__main__":
    num1 = int(input("\nEnter the First Number -> "))
    num2 = int(input("Enter the Second Number -> "))
    
    res = GCD(num1, num2)

    print("\nThe GCD of the given two Numbers is ->", res, end=" ")
    print()
