
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