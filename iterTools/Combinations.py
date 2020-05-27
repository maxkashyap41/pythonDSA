import itertools

def Comb(arr, r):
    result = []
    for item in itertools.combinations(arr, r):
        result.append(item)
    
    return result


if __name__ == "__main__":
    print("\n")
    # arr = [10,2,3,4,5,7,8]
    # r = 4
    arr = [0,0,2,1,1]
    r = 3

    res = Comb(arr, r)
    print(set(res))

    print("\n")
