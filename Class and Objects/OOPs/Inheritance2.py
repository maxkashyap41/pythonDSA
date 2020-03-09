class A:
    def __init__(self):
        print("Currently in A init.")

    def feature1(self):
        print("Feature 1-A is working.")
    
    def feature2(self):
        print("Feature 2 is working.")

class B(A):
    def __init__(self):
        super().__init__()
        super().feature1()
        print("Currently in B init.")

    def feature1(self):
        print("Feature 1-B is working.")

class C:
    def __init__(self):
        print("Currently in C init.")
    
    def miyagi(self):
        print("The ancient one.")

class D(C, A):
    def __init__(self):
        super().__init__()
        print("Currently in D init.")
    
    def feature4(self):
        print("Feature 4 is working.")




if __name__ == "__main__":
    print("\n")
    a = A()
    a.feature2()

    print("***********************************")

    b = B()
    b.feature1()

    print("***********************************")

    d = D()


    print("\n")