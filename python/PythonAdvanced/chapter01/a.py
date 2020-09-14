
def fun(name="ann"):
    print(name)

class Hello:
    def __init__(self):
        print("ann")

def Fun(name):
    return name

def fix():
    print("name")
    return Hello

if __name__ == '__main__':
    a = fun
    print("----------",a("end"))
    b = fun("hello")
    print("=============",b)
    h = Hello()
    print("***************",h)
    c = Fun("ann")
    print("00000000000", c)
    x = fix()
    print("1111111111", x)
    print("9999999999999", x())

