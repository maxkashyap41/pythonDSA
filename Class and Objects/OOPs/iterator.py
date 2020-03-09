class TopTen:
    def __init__(self):
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num = self.num+1
            return val
        else:
            raise StopIteration


if __name__ == "__main__":
    print("\n")
    values = TopTen()

    print(values.__next__())
    print(values.__next__())
    for i in values:
        print(i)
    print("\n")
