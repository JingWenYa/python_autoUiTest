print('----------------------定义-----------------')
def add(a,b,c,d=10):
    print(a+b+c+d)
add(1,2,c=3,d=4)

def add(**args):
    print(args)
add(a=1,b=2,c=3)

def add(*args):
    print(args)
add(1,2,3,4)

def add(*arg1,**arg2):
    print(arg1,arg2)
add(1,2,c=3,d=4)


print('----------------------调用-----------------')
def add(a,b,c):
    print(a+b+c)
dict = {'a':1,'b':2,'c':3}
add(**dict)

def add(a,b,c):
    print(a+b+c)
l1=[1,2,4]
add(*l1)

print('-----------------------类-------------------------')
class Study():
    def __init__(self,hour,name):
        self.hour = hour
        self.name = name
    def juan(self):
        print('卷王',self.name,'每天学习',self.hour,'小时')
    @classmethod
    def classMethod(cls):
        print('我是类方法')
    @staticmethod
    def staticMethod():
        print('我是静态方法')

stu1=Study(10,'小羊')
stu1.classMethod()
stu1.staticMethod()
stu1.juan()


print('-----------------------函数-------------------------')
print(ord('a'))
print(chr(97))

print('-----------------------exception-------------------------')

def div(a, b):
    return a/b

try:
    result = div(1,3)
except ZeroDivisionError:
    print('被除数不能为0')
except TypeError:
    print('请输入数字类型')
except BaseException as e:
    print(e)
else:
    print('a/b的结果是:',result)
finally:
    print('我是finally代码块')

