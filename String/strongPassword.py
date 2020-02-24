#   Louise joined a social networking site to stay in touch with her friends. 
#   The signup page required her to input a name and a password. 
#   However, the password must be strong. 
#   The website considers a password to be strong if it satisfies the following criteria:

#   Its length is at least 6.
#   It contains at least one digit.
#   It contains at least one lowercase English character.
#   It contains at least one uppercase English character.
#   It contains at least one special character. The special characters are: !@#$%^&*()-+
#   She typed a random string of length  in the password field but wasn't sure if it was strong. 
#   Given the string she typed, can you find the minimum number of characters she must add to make her password strong?


# input :       2
#               11
#               #HackerRank
#               3
#               Ab1
# ouput :       1
#               3
# explanation : You can make the password strong by adding 3 characters,
#               for example, $hk, turning the password into Ab1$hk which is strong. 
#               2 characters aren't enough since the length must be at least 6.

# ------------------------------------------------------------------------------------------------------------------------
#               numbers = "0123456789"
#               lower_case = "abcdefghijklmnopqrstuvwxyz"
#               upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#               special_characters = "!@#$%^&*()-+"
# ------------------------------------------------------------------------------------------------------------------------


def strongPass(string, n):
    count = 0
    if any(i.isdigit() for i in string) == False:
        count = count+1
    if any(i.isupper() for i in string) == False:
        count = count+1
    if any(i.islower() for i in string) == False:
        count = count+1
    if any("!@#$%^&*()-+" for i in string) == False:
        count = count+1
    
    minimumNumbers = max(count, 6-n)
    return minimumNumbers



if __name__ == "__main__":
    string = str(input("\nEnter the Password: "))
    n = len(string)
    res = strongPass(string, n)
    print("Minimum Number of Characters are: ", res)
    print("\n")

