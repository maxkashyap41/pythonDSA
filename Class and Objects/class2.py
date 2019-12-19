class robot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print("\nName is "+ self.name)
        print("Age is "+ str(self.age))

if __name__ == "__main__":
    r1 = robot("Max Kashyap", 21)
    r1.intro()
    
    r2 = robot("Ananya Talukdar", 21)
    r2.intro()
    