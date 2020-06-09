import math

def ClosestValue(num, divisor):
    quotient = num / divisor
    str1 = str(quotient)
    n = len(str1)

    i = 0
    while i < n-1:
        if str1[i] == '.':
            value = int(str1[i+1])
            break
        i = i+1
    
    if quotient > 0:
        if value < 5:
            x = math.trunc(quotient)
            ans = divisor * x
            return ans
        else:
            x = math.trunc(math.ceil(quotient))
            ans = divisor * x
            return ans
    else:
        if value < 5:
            x = math.trunc(quotient)
            ans = divisor * x
            return ans
        else:
            x = math.trunc(math.floor(quotient))
            ans = divisor * x
            return ans



if __name__ == "__main__":
    # num = -15         # num = 13
    # divisor = 6       # divisor = 4

    t = int(input("\nEnter the Number of TestCases: "))

    while t:
        num, divisor = map(int, input("\nEnter the Number to find the Closest value: ").split())
        ans = ClosestValue(num, divisor)
        print("Closest value to {} is {}" .format(num, ans))

        print()
        t = t-1

    print("\n")

