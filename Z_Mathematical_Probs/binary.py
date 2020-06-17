def binary(num):
    if num > 1:
        binary(num // 2)
    
    print(num % 2, end="")

def binary1(num):
    if(num > 1):
        binary1(num >> 1)
    
    print(num & 1, end="")


if __name__ == "__main__":
    print()
    no = int(input("Enter the Decimal Number: " ))
    binary(no)
    print()
    binary1(no)
    print()
