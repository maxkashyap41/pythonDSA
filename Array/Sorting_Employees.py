import operator

def Employees(nameSal, n):
    ls = []
    j = 0
    for i in range(n):
        name = nameSal[j]
        j = j+1
        salary = int(nameSal[j])
        j = j+1
        ls.append((name, salary))
    
    del i
    
    # ls = sorted(ls, key = lambda kx:(kx[1], kx[0]))
    ls = sorted(ls, key = operator.itemgetter(1, 0))

    return ls

    

if __name__ == "__main__":
    print("\n")

    n = int(input("\nEnter the Number of People: "))
    nameSal = input("Enter the Name and Salary: ").split()

    ans = Employees(nameSal, n)
    for i in range(n):
        print(ans[i][0], ans[i][1], end = ' ')
    

    print("\n")
