def Fact(num):
    if num == 0:
        return 1
    else:
        result = num * Fact(num-1)
    
    return result


def dp(n, r):
    z = n-r

    product = 1
    for i in range(1, n+1):
        product = product * i

    ans = product // (Fact(z) * Fact(r))
    return ans


if __name__ == "__main__":
    # n = 3             # n = 4
    # r = 2             # r = 2
    
    t = int(input("\nEnter the Number of Testcases: "))

    while t:
        n, r = map(int, input("Enter the n and r: ").split())
        comb = dp(n, r)
        ans = comb % 1000000007
        print("Resultant Combination is: ", ans)

        print()
        t = t-1

    print("\n")
