# This conversion I quoted down from decimal to binary in C.
# But here in the base section there will be 2.
# You can try the Decimal to Binary form using 2.

def Base10_nBase(num, base):
    i = 1
    res = 0
    while num > 0:
        res = res+(num % base)*i
        i = i*10
        num = num // base
    
    return res



if __name__ == "__main__":
    print("\n")
    # num = 711
    # base = 3
    # num = 711
    # base = 10
    num = int(input("Enter the Base10 number you wanna convert: "))
    base = int(input("Enter the desired BaseN but only <= 10: "))

    res = Base10_nBase(num, base)
    print(res)
    
    print("\n")