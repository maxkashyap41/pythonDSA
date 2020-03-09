class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def sum(self, a=None, b=None, c=None):
        sUm = 0
        if a != None and b != None and c != None:
            sUm = a+b+c
        elif a != None and b != None:
            sUm = a+b
        else:
            sUm = a
        
        return sUm
    
    def show(self):
        print(self.sum(10, 20))


if __name__ == "__main__":
    print("\n")
    objct = Student(50, 60)

    print(objct.sum(5, 9))
    objct.show()

    print("\n")
