# types of variables :~ 
#               
#                   * Instance Variable. 
#                   * Class (Static) Variable.



class Car:
    wheels = 4
    def __init__(self):
        self.mileage = 20
        self.brand = "BMW"


if __name__ == "__main__":
    print("\n")
    c1 = Car()
    c2 = Car()

    c2.mileage = 15
    c2.brand = "Honda"

    Car.wheels = 8

    print(c1.mileage, c1.brand, c1.wheels)
    print(c2.mileage, c2.brand, c2.wheels)
    print("\n")