# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# Example 2:
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

# Example 3:
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.

def LeetCode(string, k):
    result = []
    kt = k
    for i in string:
        while kt and result and result[-1] > i:
            result.pop()
            kt = kt-1
        
        result.append(i)

    print(result)

    x = ''.join(result[0:len(string)-k]).lstrip("0")
    
    if len(x):
        return x
    else:
        return 0


if __name__ == "__main__":
    print("\n")
    # string = "1432219"
    # k = 3
    # string = "9"
    # k = 1
    # string = "10200"
    # k = 1
    # string = "10"
    # k = 2
    # string = "10"
    # k = 1
    # string = "5337"
    # k = 2
    string = "1234567890"
    k = 9
    # string = "123"
    # k = 2

    ans = LeetCode(string, k)
    print(ans)

    print("\n")

