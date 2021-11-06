# input        : Money      -> 9
#                Array Size -> 6
#                Array Eles -> 1 3 4 6 7 9
#
# output       : Positions -> 2,4
# 
# explanations : return positions of the total money in array that ur pocket has
#                like i have money 9 and my pocket consists of 3,6 so i shall return
#                positions of the 3,6 like [2,4] but the index...


def iceCreamParlour(money, arr, n):
    hashmap = {}
    for i in range(n):
        key = money - arr[i]
        if key in hashmap:
            return hashmap[key]+1, i+1
        else:
            hashmap[arr[i]] = i


if __name__ == "__main__":
    money = int(input("\nEnter the Money you have: "))
    n = int(input("Enter the size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    pos1, pos2 = iceCreamParlour(money, arr, n)
    print(pos1, pos2)
    
    print("\n")

