import operator as op

if __name__ == "__main__":
    print("\n")
    hashmap = {}
    arr = [2,3,4,1,6,5]

    for idx, val in enumerate(arr):
        hashmap[val] = idx

    print(hashmap)
    print("\nHashmap in Tuples: ", hashmap.items())
    print("\nKeys of Hashmap in sorted form: ")
    for key, value in sorted(hashmap.items(), key = op.itemgetter(0)):
        print(key, "->", value, end = " ")
    
    print("\n")