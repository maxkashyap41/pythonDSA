def sumDigi(num):
    # Sum = 0
    # while num > 0:
    #     rem = num % 10
    #     Sum = Sum+rem
    #     num = num // 10
    
    # return Sum

    if num > 0:
        return (num % 10) + sumDigi(num // 10)
    else:
        return 0


if __name__ == "__main__":
    number = int(input("\nEnter the Number to find its sum: "))

    res = sumDigi(number)
    print("The SUM is ~", res)
    print("\n")