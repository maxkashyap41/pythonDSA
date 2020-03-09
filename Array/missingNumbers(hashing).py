# input :       10
#               203 204 205 206 207 208 203 204 205 206
#               13
#               203 204 204 205 206 207 205 208 203 206 205 206 204
# ouput :       204 205 206
# explanation : As an example, the array with some numbers missing, arr=[7,2,5,3,5,3].
#               The original array of numbers brr=[7,2,5,4,6,3,5,3].
#               The numbers missing are [4,6]


def missingNums(arr, brr):
    n_a = len(arr)
    n_b = len(brr)
    maxno = brr[0]
    for i in range(1, n_b):
        if maxno < brr[i]:
            maxno = brr[i]
    
    hash1 = [0]*(maxno+1)
    hash2 = [0]*(maxno+1)

    for i in range(n_a):
        hash1[arr[i]] = hash1[arr[i]]+1
    for i in range(n_b):
        hash2[brr[i]] = hash2[brr[i]]+1
    
    res = []
    for i in range(maxno+1):
        if hash1[i] == 0 and hash2[i] == 0:
            continue
        elif hash1[i] < hash2[i]:
            res.append(i)
    
    return res


if __name__ == "__main__":
    n_a = int(input("\nEnter the Array Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n_a]
    n_b = int(input("\nEnter the Brray Size: "))
    brr = list(map(int, input("Enter the Brray Elements: ").split()))[:n_b]
    
    missingResult = missingNums(arr, brr)
    
    print("\nMissing Numbers are: ", end = " ")
    for i in range(len(missingResult)):
        print(missingResult[i], end = " ")
    
    print("\n")

    