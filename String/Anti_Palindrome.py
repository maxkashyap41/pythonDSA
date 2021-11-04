def isPalindrome(string):
    length = len(string)

    j = length-1
    for i in range(length):
        if string[i] != string[j]:
            return 0
    
    return 1                # means True, so its a palindrome.


def Solve_4_largest(string):
    new_string = ''.join(sorted(string, reverse = True))
    res = isPalindrome(new_string)
    if res:
        return "-1"
    else:
        return new_string


def Solve_4_smallest(string):
    new_string = ''.join(sorted(string))
    res = isPalindrome(new_string)
    if res:
        return "-1"
    else:
        return new_string


if __name__ == "__main__":
    print("\n")
    print("  Anti-Palindrome Largest .")
    print("------------------------------")
    stringL = "caac"
    # stringL = "aba"
    # stringL = "c"

    output1 = Solve_4_largest(stringL)
    print(output1)

    
    print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
    
    
    print("  Anti-Palindrome Smallest .")
    print("------------------------------")
    string = "bpc"
    # string = "pp"
    # string = "deep"
    # string = "zyx"

    output2 = Solve_4_smallest(string)
    print(output2)

    print("\n")
