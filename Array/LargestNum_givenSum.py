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



def LargestNum(digit, Sum):
    string = ''
    i = 1
    while i < digit:
        if Sum > 9:
            Sum = Sum - 9
            string = string + '9'
            i += 1
        else:
            string = string + str(Sum)
            break
    print(i)
    print(Sum)
    if i == digit and Sum < 10:
        string = string + str(Sum)
        return string
    elif Sum < 10:
        while digit - i != 0:
            string = string + '0'
            i += 1
        return string
    else:
        return '-1'




if __name__ == "__main__":
    # print("\n")

    # digit = 3
    # Sum = 26
    # digit = 5
    # Sum = 12
    # digit = 3
    # Sum = 29

    digit, Sum = map(int, input("\nEnter the N Digit and Sum: ").split())

    # ans = LargestNum_givenSum(digit, Sum)
    ans = LargestNum(digit, Sum)
    print("The Resultant Number: ", ans)

    print("\n")