# string input -> 1,2,3,4;;;5,6,7;;;8,9,5 in the first set digital root is (1+2+3+4)=10 -> (1+0)=1
# so digital root is 1 and so in every set i.e. after ';;;' we have to find digital roots
# and then return number of evens and odds in the string


def digitalRoots(string):
    length = len(string)
    i = 0
    add = 0
    digi = []
    while i < length:
        if string[i] == ",":
            i = i+1
            continue

        if string[i] == ";":
            while add >= 10:
                rem = 0
                while add != 0:
                    rem = rem+(add%10)
                    add = add//10
                if rem <= 9:
                    digi.append(rem)
                else:
                    continue
            i = i+3
        add = add+int(string[i])
        i = i+1
    
    if add >= 10:
        while add >= 10:
            rem = 0
            while add != 0:
                rem = rem+(add%10)
                add = add//10
            if rem <= 9:
                digi.append(rem)
            else:
                continue
    
    print("Digital Roots are: ", digi)

    lenDigi = len(digi)
    even = odd = 0
    for i in range(lenDigi):
        if digi[i]%2 != 0:
            odd = odd+1
        else:
            even = even+1

    return odd, even

if __name__ == "__main__":
    string = str(input("\nEnter the String Input: "))
    ODD, EVEN = digitalRoots(string)
    print("\nOdd Numbers in the List: ", ODD)
    print("Even Numbers in the List: ", EVEN)
    print("\n")
