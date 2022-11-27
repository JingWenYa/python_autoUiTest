#
'''
面向对象三大特征
    ①封装：提高程序安全性 将属性和方法包装到类对象中  表示属性的私有->前面使用两个'_'
    ②继承：提高代码复用性
    ③多态：提高程序的可扩展性和可维护性
'''


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)


stu1 = Student('张三', 18)
stu1.show()  # 张三 18
print(stu1.name)
# print(stu1.__age)          #代码报错 'Student'类中不存在'__age'

# 想要访问类中的私有属性 使用方法dir(对象名) 查看
print(dir(stu1))             # 输出内容中与age相关的属性：'_Student__age'
print(stu1._Student__age)    # 18
