def function(num):
    if num == 0:
        return False
    
    while num != 1:
        if num%2 != 0:
            return False
        num = num//2

    return True


if __name__ == "__main__":
    no = int(input("\nEnter the Nunber: "))
    isBool = function(no)
    if not isBool:
        print("\nNO !")
    else:
        print("\nYES !")
    print("\n")