def fact(number):
    if number >= 1:
        return number * fact(number-1)
    else:
        return 1


if __name__ == "__main__":
    num = int(input("\nEnter the Number: "))
    result = fact(num)
    print("Factorial of the Given Number: ", result)
    print("\n")