#
'''
面向对象三大特征
    ①封装：提高程序安全性 将属性和方法包装到类对象中  表示属性的私有->前面使用两个'_'
    ②继承：提高代码复用性
    ③多态：提高程序的可扩展性和可维护性
'''

print('-------------------------------------------封装------------------------------------------------')
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age            #表示属性的私有->前面使用两个'_'

    def show(self):
        print(self.name, self.__age)


stu1 = Student('张三', 18)
stu1.show()  # 张三 18
print(stu1.name)
# print(stu1.__age)                #代码报错 'Student'类中不存在'__age'

# 想要访问类中的私有属性 使用方法dir(对象名) 查看
print(dir(stu1))             # 输出内容中与age相关的属性：'_Student__age'
print(stu1._Student__age)    # 18



print('-----------------------------------------------继承-----------------------------------------------------')
'''
一个类没有继承任何类 则默认继承object
python支持多继承
定义子类时 必须在其构造函数中调用父类的构造函数
方式：class 子类类名(父类1,父类2...):
'''
#定义父类
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f'姓名:{self.name},年龄:{self.age}')

#定义子类1
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score

#定义子类2
class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear

stu = Student('张三',18,100)
tea = Teacher('李四',25,5)
stu.info()      #姓名:张三,年龄:18
tea.info()      #姓名:李四,年龄:25




print('-----------------------------------------------重写-----------------------------------------------------')
'''
如果子类对继承自父类的某个属性或方法不满意 可以在子类中对其重新编写
子类重写后 调用父类被重写的方法：super().xxx()
'''

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(('姓名：%s,年龄：%s') % (self.name,self.age))

class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score = score

    #方法重写
    def info(self):
        print('学生成绩',self.score)

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear

    #方法重写
    def info(self):
        print('老师教龄',self.teachofyear)
        super().info()

stu1=Student('学生',18,100)
stu1.info()                 #学生成绩 100
tea1=Teacher('老师',35,10)
tea1.info()                 #老师教龄 10   姓名：老师,年龄：35




print('-----------------------------------------------object类----------------------------------------------------')
'''
Object是所有类的父类
内置函数dir()：可以查看指定对象的所有属性
__str()__方法：返回‘对象的描述’ 一般会对str()方法进行重写 方便查看对象的信息
'''

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名：{0}，年龄：{1}'.format(self.name,self.age)

stu = Student('张三',19)
print(dir(stu))
print(stu)          #姓名：张三，年龄：19   从写str()方法后 不再输出内存地址 而是调用重写后的方法
print(type(stu))    #<class '__main__.Student'>





print('-----------------------------------------------多态----------------------------------------------------')
'''

'''
class Animal():
    def eat(self):
        print('动物会吃')

class Dog(Animal):
    def eat(self):
        print('狗吃肉')

class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Person:
    name = "per"

    def __init__(self, age):
        self.age = age

    def eat(self):
        print('人吃五谷杂粮')

    def run(self):
        self.eat()

def fun(obj):
    obj.eat()

#方法调用
p = Person

fun(Person)   #人吃五谷杂粮
fun(Cat())      #猫吃鱼
fun(Dog())      #狗吃肉
fun(Animal())   #动物会吃




print('---------------------------------------------特殊属性和方法----------------------------------------------------')
#属性：__dict__    获得类对象或实例对象所绑定的所有属性和方法的字典
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
#创建c的对象
c=C('jack',20)
print(c.__dict__)   #实例对象的属性字典 {'name': 'jack', 'age': 20}
print(C.__dict__)   #类对象的属性和方法字典 {'__module__': '__main__', '__init__': <function C.__init__ at 0x0000021602AB4C18>, '__doc__': None}

#方法：__class__()  获取类或对象的类型
print(c.__class__)  #<class '__main__.C'>
print(C.__class__)  #<class 'type'>

#方法：__bases__()  获取父类类型的元组
print(C.__bases__)  #(<class '__main__.A'>, <class '__main__.B'>)

#方法：__base__()  获取第一个父类类型的元组 类的基类
print(C.__base__)   #<class '__main__.A'>

#方法：__mro__()  获取该类的父类层次结构
print(C.__mro__)    #(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

#方法：__subclasses__()  获取类的子类列表
print(A.__subclasses__())   #[<class '__main__.C'>]

#方法：__len__()   通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
class Student:
    def __init__(self,name):
        self.name = name
    def __len__(self):
        return len(self.name)

s1=Student('张三1')
print(len(s1))      #3


#方法：__add__()   通过重写__add__()方法，可使自定义对象具有’+‘功能
class Student:
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        return self.name+ other.name

s1=Student('张三')
s2=Student('李四')
print(s1+s2)               #张三李四
print(s1.__add__(s2))      #张三李四

#方法：__new__()   用于创建对象


#方法：__init__()  对创建的对象进行初始化