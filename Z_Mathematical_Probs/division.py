def division(num1, num2):
    res = num1 / num2
    return res

if __name__ == "__main__":
    a = int(input("\nEnter the First Number: "))
    b = int(input("Enter the Second Number: "))

    print("The FOLLOWING RESULT is ->", division(a, b), end=" ")
    print()


# if __name__ == "__main__":
#     a = [[1, 2], [3, 4]]
#     print("\n", sum(a,[]))