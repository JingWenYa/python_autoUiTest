print('----------------------------------------类的创建---------------------------------------------------')
#class关键字 类名遵循驼峰命名
class Student:
    native_space='陕西'   #直接写在类里的属性 -->类属性
    def __init__(self,name,age):
        self.name = name    #self_name称为实体属性
        self.age = age

    #实例方法
    def eat(self):          #self指的是 实例的对象
        print('在吃饭...')

    #静态方法
    @staticmethod
    def staic_method():
        print('我是静态方法 用staicmethod修饰')

    #类方法
    @classmethod
    def class_method(cls):          #
        print('我是类方法 用classmethod修饰')


#在类之外的定义的称为函数 类之内定义的称为方法
def drink():
    print('喝东西...')

#定义了类 即开辟了内存空间
print(id(Student))      #1766793787448
print(type(Student))    #<class 'type'>
print(Student)          #<class '__main__.Student'>



print('---------------------------------------对象的创建---------------------------------------------------')
# 实例名=类名()   对象的创建即类的实例化
#创建Student类的对象
stu1=Student('张三',20)

print(id(stu1))             #2312645474504
print(type(stu1))           #<class '__main__.Student'>
print(stu1)                 #<__main__.Student object at 0x0000021A746978C8>



print('---------------------------------------对象的调用---------------------------------------------------')
stu1=Student('李四',25)
#调用实例方法一  对象.方法()
stu1.eat()              #在吃饭...
#调用实例方法二  类.方法(对象)
Student.eat(stu1)       #在吃饭...
#调用实例属性
print(stu1.name)    #李四



print('---------------------------------------类属性的使用---------------------------------------------------')
#类属性：类中方法外，被该类所有对象共享
class Student:
    native_space='陕西'   #直接写在类里的属性 -->类属性

#方式一 类名.属性名
print(Student.native_space)  #陕西

#方式二  对象.属性名
stu2=Student()
print(stu2.native_space)    #陕西
#修改类属性值 对象调用时修改生效
Student.native_space='厦门'
print(stu2.native_space)    #厦门



print('---------------------------------------类方法的使用---------------------------------------------------')
#使用@classmethod修饰的方法 可以使用类名直接访问的方法(类和对象均可以调用的方法)
class Student:
    #类方法
    @classmethod
    def class_method(cls):          #
        print('我是类方法 用classmethod修饰')

#方式一  类名.类方法()
Student.class_method()      #我是类方法 用classmethod修饰

#方式二  对象名.类方法()
stu3 = Student()
stu3.class_method()         #我是类方法 用classmethod修饰




print('---------------------------------------静态方法的使用---------------------------------------------------')
#使用@classmethod修饰的方法 使用类名直接访问的方法(类和对象均可以调用的方法)
class Student:
    #静态方法
    @staticmethod
    def staic_method():
        print('我是静态方法 用staicmethod修饰')

#方式一  类名.静态方法()
Student.staic_method()      #我是静态方法 用staicmethod修饰

#方式二  对象名.静态方法()
stu3 = Student()
stu3.staic_method()         #我是静态方法 用staicmethod修饰




print('---------------------------------------动态绑定属性和方法---------------------------------------------------')
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',20)
stu2=Student('李四',25)

'''动态绑定属性'''
stu1.gender='男'     #只适用于当前绑定的对象
print(stu1.name,stu1.age,stu1.gender)   #张三 20 男
print(stu2.name,stu2.age)               #李四 25

'''动态绑定方法'''
def show():
    print('定义在类之外，称为函数')

stu1.show=show      #动态绑定方法
stu1.show()         #定义在类之外，称为函数

