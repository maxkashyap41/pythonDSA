# input       : 1, 2, 3, 7, 5 
#               Sum ~ 12
# output      : Positions 2 and 4
# explanation : basically runs on the sliding window protocol.

def subArrayGivenSum(arr, n, k):
    pass


if __name__ == "__main__":
    print("\n")

    arr = [1,2,3,7,5]
    k = 12
    # arr = [1,2,3,4,5,6,7,8,9,10]
    # k = 15
    # arr = [2,3,7,8]
    # k = 7
    # arr = [2,3,7,8]
    # k = 11
    # arr = [1,2,7,22,61,3,4,1]
    # k = 5
    n = len(arr)

    n, k = map(int, input("\nEnter the Size and Sum 'k': ").split())
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    
    # if subArray(arr, n, k) == -1:
    #     print("-1")
    # else:
    #     start, end = subArray(arr, n, k)
    #     print("Position at: ", start+1, end+1)

    if subArrayGivenSum(arr, n, k) == -1:
        print("-1")
    else:
        start, end = subArrayGivenSum(arr, n, k)
        print("Position at: ", start, end)

    print("\n")