# Enter the 1st Term and 2nd Term: -6 28        Enter the 1st Term and 2nd Term: 2 5
# Enter the Nth number to find the GP: 3        Enter the Nth number to find the GP: 7
# The GP of the 3th term is : -131              The GP of the 7th term is : 488

# gp7 = a1 * r^(7-1)
# 7 is the n term a1 is the 1st term no. whereas r is the common ratio between every numbers
# 2 4 8 16 32 64 128 so here the common ration is r. (a1, a2, a3, ...., a(n)). 128 is the 7th term gp.

import math

def SeriesGP(a1, a2, n):
    common_ratio = a2 / a1
    nth = n-1
    ans = a1 * pow(common_ratio, nth)
    
    gp = math.floor(ans)

    return gp

if __name__ == "__main__":
    t = int(input("\nEnter the Testcases: "))
    
    while t:
        a1, a2 = map(int, input("\nEnter the 1st Term and 2nd Term: ").split())
        n = int(input("Enter the Nth number to find the GP: "))
        
        gp = SeriesGP(a1, a2, n)
        print("The GP of the {}th term is : {}" .format(n, gp))
        
        t = t-1
    
    print("\n")

    