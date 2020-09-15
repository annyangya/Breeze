
class Hello:
    def __init__(self, info_list):
        self.info_list = info_list

    def __getitem__(self, item):
        return self.info_list[item]

    def __len__(self):
        return len(self.info_list)

hello = Hello([1,2,3,4])
print(len(hello)) # 4, 如果没有在这个类中定义len方法，就不能对hello进行len操作：TypeError: object of type 'Hello' has no len()


"""使用getitem魔法函数，会在没有迭代器的情况下，去依次获取元素，相当于迭代，没有getitem函数则只是一个类对象，不可迭代"""

class Model:
    def __init__(self, info_list):
        self.info_list = info_list

    def __str__(self):
        return ",".join(self.info_list)

    def __repr__(self):
        return ",".join(self.info_list)

m = Model(["as", "dd", "vv"])
print(m) # as,dd,vv
print(m) # <__main__.Model object at 0x114cf3ba8>
