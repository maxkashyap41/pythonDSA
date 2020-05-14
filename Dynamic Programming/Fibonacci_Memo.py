def Fib(num, memo):
    if memo[num] != None:
        return memo[num]
    
    if num == 1 or num == 2:
        result = 1
    else:
        result = Fib(num-1, memo)+Fib(num-2, memo)
    
    memo[num] = result
    return result


if __name__ == "__main__":
    num = int(input("\nEnter the Number: "))
    memo = [None]*(num+1)
    res = Fib(num, memo)
    print("Given Number Fibonacci Number is: ", res)
    print("\n")