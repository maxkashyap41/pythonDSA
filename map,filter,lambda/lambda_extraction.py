# ls = sorted(ls, key = lambda kx:(kx[1], kx[0]))
# breaking lambda kx:(kx[1], kx[0])


def myfunc(arr, n):
    result = []
    ele = arr[0][1]
    chck = True
    for x in arr:
        if ele != x[1]:
            chck = False
            break
    
    for x in arr:
        if chck == True:
            result.append(x[0])
            result.append(x[1])
        else:
            result.append(x[1])
            result.append(x[0])
        
    return result

if __name__ == "__main__":
    print("\n")

    # arr = [('Max', 10), ('Ehru', 10), ('Ani', 10)]
    arr = [('Max', 10), ('Ehru', 5), ('Ani', 1)]
    n = len(arr)

    res = myfunc(arr, n)
    print(res)

    print("\n")