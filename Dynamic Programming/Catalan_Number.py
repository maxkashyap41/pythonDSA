def Catalan(num, memo):
    key = num
    if key in memo:
        return memo[key]
    
    if num == 0 or num == 1:
        return 1

    result = 0
    for i in range(0, num):
        result = result + (Catalan(i, memo)*Catalan(num-i-1, memo))
    
    memo[key] = result
    return result


if __name__ == "__main__":
    print("\n")

    # num = 4
    # num = 5
    # num = 10
    num = int(input("Enter the Number in which you wanna find the Catalan: "))
    memo = {}
    res = Catalan(num, memo)
    print("{} has catalan Number of: {}" .format(num, res))

    print("\n") 