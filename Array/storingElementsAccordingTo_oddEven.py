# Explanation :- Sorting all even index placed elements in ascending 
#                and Sorting all odd index placed elements in Descending.

def storingOddEven(arr, n):
    even = []
    odd = []
    for i in range(n):
        if i % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    
    even.sort()
    odd.sort(reverse = True)

    j = 0
    k = 0
    for i in range(0,n):
        if i % 2 ==0:
            arr[i]=even[j]
            j=j+1
        else:
            arr[i]=odd[k]
            k=k+1

    return arr


if __name__ == "__main__":
    n = int(input("\nEnter the Array Size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    res = storingOddEven(arr, n)
    print("\nSorted List: ", end = " ")
    for i in range(len(res)):
        print(res[i], end = " ")
    print("\n")


