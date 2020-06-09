import numpy as np

if __name__ == "__main__":
    print("\n")
    
    arr = np.array([1,2,3,4,5,6,7,8,10])
    brr = np.arange(0, 20, 2)
    crr = np.logspace(2, 4, 5)      # the 4 is meant to be 10 raise to 4.
    drr = np.zeros(10, int)         # int because by-default float gets created.
    err = np.ones(20, int)
    frr = np.linspace(2, 3, 20)     # 2 to 3 thats the range but it should consist 20 values

    print(arr)
    print(brr)
    print(crr, "\n")
    print('%.4f' %crr[1])
    print(drr)
    print(err)
    print(frr)

    print("\n")