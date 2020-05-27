def LargestNum_givenSum(digit, Sum):
    result = []
    if Sum > (9*digit) or Sum == 0:
        return -1
    else:
        while Sum > 9:
            result.append(9)
            Sum = Sum-9
        result.append(Sum)
    
    
    if len(result) == digit:
        x = ''.join(map(str, result))
        return int(x)
    elif len(result) < digit:
        n = digit-len(result)
        for i in range(n):
            result.append(0)
        del i
            
        x = ''.join(map(str, result))
        return int(x)



if __name__ == "__main__":
    # print("\n")

    # digit = 3
    # Sum = 26
    # digit = 5
    # Sum = 12
    # digit = 3
    # Sum = 29

    digit, Sum = map(int, input("\nEnter the N Digit and Sum: ").split())

    ans = LargestNum_givenSum(digit, Sum)
    print("The Resultant Number: ", ans)

    print("\n")