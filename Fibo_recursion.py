def fibonacci(index_num):
    if index_num >= 3:
        return fibonacci(index_num-1) + fibonacci(index_num-2)
    else:
        return 1


if __name__ == "__main__":
    number = int(input("\nEnter the Desired Fibonacci Number: "))
    result = fibonacci(number)
    print("The opted Fibonacci Number is ~ ", result)
    print("\n")