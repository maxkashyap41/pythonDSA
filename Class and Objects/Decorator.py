# Decorators are used to change any existing function features and behaviour at the compile time. 
#                                                           
#                                                                                                   ~ by Telusko


def div(a, b):
    print(a/b)

def smart_div(func):
    def inner(a, b):
        if a < b:
            a,b = b,a
        return func(a, b)
    return inner

if __name__ == "__main__":
    print("\n")
    div = smart_div(div)
    div(2,4)
    print("\n")
