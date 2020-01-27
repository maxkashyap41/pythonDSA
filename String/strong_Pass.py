def strongPass(string, n):
    count = 0
    if any(i.isdigit() for i in string) == False:
        count = count+1
    if any(i.isupper() for i in string) == False:
        count = count+1
    if any(i.islower() for i in string) == False:
        count = count+1
    if any(i in '!@#$%^&*()-+' for i in string) == False:
        count = count+1
    
    maxno = max(count, 6-n)
    return maxno


if __name__ == "__main__":
    string = str(input("\nEnter the Password: "))
    n = len(string)
    res = strongPass(string, n)
    print("Minimum Number of Characters are: ", res)
    print("\n")

