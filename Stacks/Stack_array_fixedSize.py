class EmptyStackError(Exception):
    pass

class FullStackError(Exception):
    pass

class Stack:
    def __init__(self, maxsize):
        self.arr = [None]*maxsize
        self.count = 0
    
    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.arr)

    def stackSize(self):
        return self.count

    def Push(self, items):
        if self.isFull():
            raise FullStackError("\nOverFlow !")

        self.arr[self.count] = items
        self.count = self.count+1
    
    def Pop(self):
        if self.isEmpty():
            raise EmptyStackError("\nUnderFlow !")
        
        x = self.arr[self.count-1]
        self.arr[self.count-1] = None
        self.count = self.count-1
        return x

    
    def Peek(self):
        if self.isEmpty():
            raise EmptyStackError("\nUnderFlow !")

        return self.arr[self.count-1]

    def Display(self):
        print(self.arr)


if __name__ == "__main__":
    obj = Stack(5)

    print("\n-------------------- STACK --------------------\n")

    while True:
        print("\n\n1. Push Items in the Stack.")
        print("2. Pop Items.")
        print("3. Size of the Stack.")
        print("4. Peek value of Stack.")
        print("5. Display.")
        print("6. Quit.")

        option = int(input("\nChoose any one option: "))
        if option == 1:
            items = int(input("Enter the Items you wanna Push into the Stack: "))
            obj.Push(items)
            print("\nItem Pushed !")
        elif option == 2:
            value = obj.Pop()
            print("{} Poped !" .format(value))
        elif option == 3:
            res = obj.stackSize()
            print("\nSize of the  Stack is: ", res)
        elif option == 4:
            value = obj.Peek()
            print("\nItem at the Top of the Stack is: ", value)
        elif option == 5:
            obj.Display()
        elif option == 6:
            break
        else:
            print("\nWrong choice try again !!")

    print("\n")