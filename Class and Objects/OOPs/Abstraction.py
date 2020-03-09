# Data Abstraction has ~
#                      
#                      * Abstract Class
#                      * Abstact Methods


from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def cpu(self):
        pass

class Laptop(Computer):
    def cpu(self):
        print("It's been Running in Laptop.")

class Desktop:
    def gpu(self):
        print("It's been Running in Desktop.")

class Programmer:
    def work(self, tool):
        print("Problem Solving.")
        tool.gpu()


if __name__ == "__main__":
    print("\n")
    # com = Computer()
    lap = Laptop()
    lap.cpu()

    desk = Desktop()

    prog = Programmer()
    prog.work(desk)
    print("\n")