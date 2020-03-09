# Inner Class -> Class inside a class (nested class).


class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.addr = self.Address()      # creating object of inner class inside the outer class.
    
    def show(self):
        print("Name:", self.name)
        print("RollNo:", self.rollno)
        self.addr.showAddr()
    
    class Laptop:
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
        
        def show(self):
            print(self.brand, self.cpu, self.ram)
    
    class Address:
        def __init__(self):
            self.address = 'NR Colony, JeevanBima Nagara'
        
        def showAddr(self):
            print("Location: ", self.address)


if __name__ == "__main__":
    print("\n")
    s1 = Student('Max', 1628041)
    s2 = Student('Ehraz', 1628042)

    lap1 = s1.Laptop('Dell', 'i7', '8GB')       # creating the inner class objects outside the outer class. 
    lap2 = s2.Laptop('Lenovo', 'i5', '8GB')

    s1.show()
    lap1.show()
    print("*******************************************")
    s2.show()
    lap2.show()
    print("\n")

