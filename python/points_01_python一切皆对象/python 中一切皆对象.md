#### python 中一切皆对象

##### 对象的定义

Java中class和object的定义，object是class的一个实例

python中一切皆对象，函数和类也是对象，python语言动态性的体现 ，python面向对象更加彻底

##### 函数和类也是对象

- 赋值给一个变量
- 可以添加到集合对象中
- 可以作为参数传递给函数
- 可以作为函数的返回值

```python
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
    
"""
end
---------- None
hello
============= None
ann
*************** <__main__.Hello object at 0x10cbf8b70>
00000000000 ann
name
1111111111 <class '__main__.Hello'>
ann
9999999999999 <__main__.Hello object at 0x10cbf8ba8>
"""
```

#### type, object, class 的关系

```python
a = 1
print(type(a))
print(type(1))
print(type(int))
print("----------------------")
s = "ann"
print(type(s))
print(type(str))
print(type(type))

print('-------------------')
class Hello():
    pass
hello = Hello()
print(type(hello))
print(type(Hello))

"""
class类是由type这个类生成的对象 ，平常熟悉的对象是由类对象创建的对象，类又是由type创建的

object是所有类都要继承的顶层的类
"""
print("-----------------")
class Student:
    pass
class myStudent(Student):
    pass

stu = Student()
print(type(stu))
mstu = myStudent()
print(type(mstu))
print(type(Student))
print(type(myStudent))

print("----------------基类")
print(Student.__bases__)
print(myStudent.__bases__)
print(int.__bases__)
print(type.__bases__)
print(object.__bases__)
print(type(object))

"""
<class 'int'>
<class 'int'>
<class 'type'>
----------------------
<class 'str'>
<class 'type'>
<class 'type'>
-------------------
<class '__main__.Hello'>
<class 'type'>
-----------------
<class '__main__.Student'>
<class '__main__.myStudent'>
<class 'type'>
<class 'type'>
----------------基类
(<class 'object'>,)
(<class '__main__.Student'>,)
(<class 'object'>,)
(<class 'object'>,)
()
<class 'type'>
"""
```

**python中一切皆对象，所有类都是type的实例，包括type自己，包括object，即所有类都是type 的对象。**

**python中object是一切类的基类，type的基类也是object， object的基类是空。**

**所有类示type的实例，object是所有类的基类**

![屏幕快照 2020-09-14 21.32.58](/Users/apple/githup/Breeze/python/points_01_python一切皆对象/屏幕快照 2020-09-14 21.32.58.png)

#### python 中常见的内置类型

- None(全局只有一个)
- 数值类型
  - int, float, complex, bool
- 迭代类型
- 序列类型
  - list, tupple, str, bytes, array
- 映射（dict）
- 集合 （set，frozenset）
  - set无序排序且不重复，是可变的，有add（），remove（）等方法。既然是可变的，所以它不存在哈希值。基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交集), difference(差集)和sysmmetric difference(对称差集)等数学运算.  
    sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, 或其它类序列的操作。
    frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。缺点是一旦创建便不能更改，没有add，remove方法。
- 上下文管理器（with）
- 其他