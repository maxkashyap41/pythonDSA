class Pycharm:
    def execute(self):
        print("Compiling.")
        print("Running.")
    
class VScode:
    def execute(self):
        print("Spell Check.")
        print("Convention Check.")
        print("Compiling.")
        print("Running.")

class Laptop:
    def code(self, ide):
        ide.execute()


if __name__ == "__main__":
    print("\n")
    # ide = Pycharm()
    ide = VScode()

    lap = Laptop()
    lap.code(ide)
    print("\n")