def func(a, b):
    hashmap = {}

    Sum = a+b
    hashmap[Sum] = (a,b)

    print(hashmap)


if __name__ == "__main__":
    print("\n")
    a = 10
    b = 20
    
    func(a, b)

    print("\n")