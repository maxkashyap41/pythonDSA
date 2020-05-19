def Base10_nBase(num, base):
    i = 1
    res = 0
    while num > 0:
        res = res+(num % base)*i
        i = i*10
        num = num // base
    
    return res



def FooBar(n, b):
    count = 0
    result = []
    flag = -1
    
    while True:
        x = ''.join(sorted(str(n), reverse=True))
        y = ''.join(sorted(str(n)))

        x_ten = int(x, b)
        y_ten = int(y, b)

        z_ten = x_ten - y_ten
        z = Base10_nBase(z_ten, b)
        
        
        if len(result) == 0:
            result.append(z)
            n = z
        else:
            for i in range(len(result)):
                if result[i] == z:
                    flag = 1
                    j = i
                    while j < len(result):
                        count = count+1
                        j = j+1
        
            if flag == 1:
                return count
            else:
                result.append(z)
                n = z

if __name__ == "__main__":
    print("\n")
    # n = '1211'
    # b = 10
    # n = '210022'
    # b = 3
    n = str(input("Enter the ID for the Minion: "))
    base = int(input("Enter the Base you wanna suggest: "))
    res = FooBar(n , base)
    print("Result: ", res)

    print("\n")
