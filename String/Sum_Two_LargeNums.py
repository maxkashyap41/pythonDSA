# Given two non-negative numbers X and Y.
# The task is calculate the sum of X and Y.
# If the number of digits in sum (X+Y) are equal to the number of digits in X,
# then print sum, else print X.


def Sum_LargeNums(x, y):
    Result = x+y

    res_St = str(Result)
    x_St = str(x)

    if len(res_St) == len(x_St):
        res = int(res_St)
    else:
        res = int(x)
    
    return res


if __name__ == "__main__":
    # x = 25
    # y = 23
    # x = 100
    # y = 1000
    t = int(input("\nEnter the Number of Testcases: "))

    while t:
        x, y = map(int, input("Enter the X and Y: ").split())
        ans = Sum_LargeNums(x, y)
        print("\nThe Resultanat Answer is: ", ans)

        t = t-1

    print("\n")