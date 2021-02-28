# types of methods :~ 
#               
#                   * Instance Methods. 
#                   * Class Methods.
#                   * Static Methods.


class Student:
    college = "YouTube."

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        return (self.m1+self.m2+self.m3) / 2
    
    # getter method also known as accessors
    def get_m1(self):
        return self.m1
    
    # setter method also known as mutators
    def set_m2(self, value):
        self.m2 = value
        return self.m2
    
    # class methods
    @classmethod
    def CollegeInfo(cls):
        return cls.college
    
    # static methods
    @staticmethod
    def CobraKai_s04():
        print("When will COBRA-KAI season 4 will release...... !!!")
    
    @staticmethod
    def CobraKai_s03():
        print("COBRA-KAI season 3 was dawn awesome...... waiting for S04....!!!")

if __name__ == "__main__":
    print("\n")
    s1 = Student(67, 65, 72)
    s2 = Student(88, 89, 90)

    print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("//------------- INSTANCE METHODS -------------//")
    print(s1.avg())
    print(s2.avg())

    print(s1.get_m1())
    print(s2.get_m1())

    print(s1.set_m2(100))
    print(s2.set_m2(99))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")


    print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("//------------- CLASS METHODS -------------//")
    print(s1.avg())
    print(s2.avg())

    print(Student.CollegeInfo())
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")


    print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("//------------- STATIC METHODS -------------//")
    print(s1.avg())
    print(s2.avg())

    Student.CobraKai_s04()
    Student.CobraKai_s03()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

    print("\n")
