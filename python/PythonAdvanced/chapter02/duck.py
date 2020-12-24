
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]
d = {"boy":"as","girl":"sa"}
a.extend(d)
print(a)  # [1, 2, 3, 4, 5, 6, 'boy', 'girl']
a.extend("hello")
print(a)  # [1, 2, 3, 4, 5, 6, 'boy', 'girl', 'h', 'e', 'l', 'l', 'o']

class Fun:
    # 初始化
    def __init__(self, info_list):
        self.info_list = info_list
    # 可迭代的
    def __getitem__(self, item):
       return self.info_list[item]
    # 输出内容
    def __str__(self):
        return ",".join(self.info_list)
f = Fun(["12aa","12bb"])
print(f)    # 12aa,12bb， __str___
a.extend(f)  # __getitem__
print(a)  # [1, 2, 3, 4, 5, 6, 'boy', 'girl', 'h', 'e', 'l', 'l', 'o', '12aa', '12bb']
# 只要添加可迭代的对象，就会对这个对象遍历然后将元素添加到里面去

class Boy:
    def eat(self):
        print("boy like eating")

class Girl:
    def eat(self):
        print("girl like eating")

s_info = [Boy, Girl]
for s in s_info:
    s().eat()
    """
    boy like eating
    girl like eating
    在  python中，只要类有这个方法，就可以被调用，而不用说必须继承什么的 
    """