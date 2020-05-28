import itertools

def findFour(arr, k):
    result = []

    for items in itertools.combinations(arr, 4):
        if sum(items) == k:
            result.append(items)
    
    return result


if __name__ == "__main__":
    # print("\n")
    # arr = [10,2,3,4,5,7,8]
    # k = 23
    # arr = [0,0,2,1,1]
    # k = 3

    t = int(input())
    while t:
        n, k = map(int, input("\nEnter the Size and Sum: ").split())
        arr = list(map(int, input("Enter the Array Elements: ").split()))[:n]

        found = False
        res = findFour(sorted(arr), k)
        # print(res)
        main = []
        for i in res:
            if i not in main:
                main.append(i)

        print("\nResult:", end = ' ')
        for obs in main:
            found = True
            print(obs[0], obs[1], obs[2], obs[3], "$",end = "")
        print(-1 if not found else '')

        t = t-1

    print("\n")