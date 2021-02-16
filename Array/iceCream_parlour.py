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
    i = 0
    add = 0
    found = -1
    pos = []
    while i < n:
        for j in range(i+1, n):
            add = arr[i]+arr[j]
            if add == money:
                found = True
                break
        if found == True:
            break
        else:
            i = i+1
    pos.append(i+1)
    pos.append(j+1)
    return pos


if __name__ == "__main__":
    money = int(input("\nEnter the Money you have: "))
    n = int(input("Enter the size: "))
    arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]
    positions = iceCreamParlour(money, arr, n)
    print(positions)
    print("Positions are: ", end = " ")
    print(' '.join(map(str, positions)))
    print("\n")

