class A:
    def feature1(self):
        print("Feature 1 is working.")
    
    def feature2(self):
        print("Feature 2 is working.")

class B(A):                             # single inheritance
    def feature3(self):
        print("Feature 3 is working.")
    
    def feature4(self):
        print("Feature 4 is working.")

class C(B):                             # multilevel inheritance
    def feature5(self):
        print("Feature 5 is working.")

class D:
    def CSSE(self):
        print("Im from CSSE but CSE.")
    
class E:
    def CSCE(self):
        print("Im from CSCE but CSE.")

class F(D, E):                          # multiple inheritance
    def CSE(self):
        print("Im from CSE.")



if __name__ == "__main__":
    print("\n")
    a = A()
    a.feature1()

    b = B()
    b.feature2()

    c = C()
    c.feature3()

    d = D()
    d.CSSE()

    e = E()
    e.CSCE()

    f = F()
    print("for f objct ~")
    f.CSSE()
    f.CSCE()
    f.CSE()

    print("\n")