class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self, otherStud):
        m1 = self.m1 + otherStud.m1
        m2 = self.m2 + otherStud.m2
        res = Student(m1, m2)
        return res
    
    def __gt__(self, otherStud):
        s1 = self.m1 + self.m2
        s2 = otherStud.m1 + otherStud.m2

        if s1 > s2:
            return True
        else:
            return False
    
    def __str__(self):
        return '{} {}'. format(self.m1, self.m2)
    


if __name__ == "__main__":
    print("\n")
    s1 = Student(60, 89)
    s2 = Student(52, 97)

    res = s1+s2
    print(res.m1)
    print(res.m2)
    print(res)

    print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n")
    
    if s1 > s2:
        print("S1 wins ! K.O.")
    else:
        print("S2 wins ! K.O.")
    
    print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n")

    print(s1)

    print("\n")