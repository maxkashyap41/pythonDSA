class robot:
    def intro(self):
        print("\nName is "+ self.name)
        print("Gender is "+ self.sex)
        print("Color is "+ self.color)

if __name__ == "__main__":
    r1 = robot()
    r1.name = "Max Kashyap"
    r1.sex = "Male"
    r1.color = "blue"

    r2 = robot()
    r2.name = "Ananya Talukdar"
    r2.sex = "Female"
    r2.color = "pink"

    r1.intro()
    r2.intro()