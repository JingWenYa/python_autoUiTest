print('-------------------------------------函数的创建-----------------------------------------')
#def 函数名([输入参数]):
#    函数体
#    [renturn xxx]
def calc(a,b): #a和b为形参 出现位置；函数定义处
    c=a+b
    return c


print('-------------------------------------函数的调用-----------------------------------------')

'''
位置实参
'''
result = calc(10,30) #10和30为实参 出现位置：函数的调用处
print(result)

'''
关键字实参
'''
result = calc(b=10,a=30)
print(result)


print('-------------------------------------------函数的调用修改-------------------------------------------------')
def fun(arg1,arg2):
    print(arg1,arg2) #11 [22, 33, 44]
    arg1=100
    arg2.append(10)
    print(arg1, arg2) #100 [22, 33, 44, 10]

n1=11
n2=[22,33,44]
fun(n1,n2)
print(n1,n2) #11 [22, 33, 44, 10]

#结论：在函数调用过程中修改参数值：不可变对象->修改后不影响实参数值  可变对象->修改后会影响实参值



print('---------------------------------------------函数的返回值-----------------------------------------------------')
'''
函数的返回值
    ① 函数没有返回值：return可以不写
    ② 函数返回值为1个：直接返回类型
    ③ 函数返回值为多个：返回结果为元组
'''

#定义函数
def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


# 调用函数
lst = [10, 29, 34, 23, 44, 53, 55]
print(fun(lst))  # ([29, 23, 53, 55], [10, 34, 44]) -元组




print('------------------------------------------定义函数时：函数的参数定义-----------------------------------------------')
'''
函数定义时 给形参设置默认值：
    函数调用时：不传对应的实参->形参使用默认值
               传对应的实参->形参使用传入的值
'''

def fun(a,b=10):
    print(a,b)

fun(100) #100 10
fun(20,30) #20 30


'''
个数可变的位置参数：
    定义参数时 无法确定传递的位置实参个数时，使用可变的位置参数
    使用*定义可变的位置形参
    结果为一个元组
'''
def fun(*args): #函数定义时 可变的位置参数
    print(args)

fun(10)        #(10,)
fun(10,30)     #(10, 30)
fun(10,30,50)  #(10, 30, 50)


'''
个数可变的关键字形参：
    定义参数时 无法确定传递的关键字实参个数时，使用可变的关键字形参
    使用*定义可变的关键字形参
    结果为一个字典
'''
def fun(**args): #函数定义时 可变的关键字形参

    print(args)

fun(a=10) #{'a': 10}
fun(a=100,b=300,c=500) #{'a': 100, 'b': 300, 'c': 500}

# def fun(*args,*a):  #代码报错，可变的位置参数只能定义一个
# def fun(**args,**a):  #代码报错，可变的关键字参数只能定义一个
# def fun(**args,*a):  #代码报错，可变的关键字参数只能定义一个
# def fun(*args,**a):  #代码不报错

'''
定义函数，个数可变的关键字形参和位置形参同时存在时，要求：个数可变的位置形参 在 个数可变的关键字形参之前
'''




print('------------------------------------------调用函数时：函数的参数传递-----------------------------------------------')
def fun(a,b,c):
    print('a=',a,'b=',b,'c=',c)

fun(10,20,30)    #a= 10 b= 20 c= 30  #位置实参
#用列表传参
lst=[40,50,60]
#fun(lst)        #代码报错，参数缺少
fun(*lst)        #a= 40 b= 50 c= 60   个数可变的位置实参 调用时 将列表的每个元素都转为位置实参传入
#用元组传参
t1=(10,20,300)
fun(*t1)        #a= 10 b= 20 c= 300


fun(a=10,b=20,c=30)  #a= 10 b= 20 c= 30 关键字实参
#用字典传参
dict1={'a':111,'b':222,'c':333}
#fun(dict1)      #报错 参数缺少
fun(**dict1)     #a= 111 b= 222 c= 333  个数可变的关键字实参 调用时 将字典中的键值对都转为关键字实参传入

#关键字实参和位置传参一起使用
fun(10,b=20,c=30)    #a= 10 b= 20 c= 30  位置传参和关键字实参一起使用(位置传参需在关键字传参前)

#后几个参数只能使用关键字传参
def fun(a,b,*,c,d):   #加星-> 后面的参数只能用关键字传参
    print('a=',a,'b=',b,'c=',c,'d=',d)
#fun(10,20,30,d=40) #报错 函数定义参数加星后 后面的参数只能用关键字传参
fun(10,20,c=30,d=400) #a= 10 b= 20 c= 30 d= 400



print('------------------------------------------函数调用时的形参顺序-----------------------------------------------')
def fun(a,b,*,c,d,**args):
    pass

def fun(*arg1,**arg2):
    pass

def fun(a,b=10,*arg1,**arg2):
    pass



print('------------------------------------------变量的作用域-----------------------------------------------')
#局部变量
def fun(a,b):
    c=a+b       #c为局部变量
    print(c)

#print(c) #报错 超出了c的作用域
#print(a) #同上

#全局变量
apple='苹果'
def fun_apple():
    print(apple)

fun_apple()     #apple的作用范围：函数的内部和外部均可使用 -->称为全局变量


#变为全局变量  使用global定义
def fun_name():
    global name     #局部变量使用了global声明 会变为全局变量
    name='lily'
    print(name)

fun_name()
print(name) #报错 name为fun_name的局部变量  -->使用global定义name 即变为全局变量





print('------------------------------------------递归函数-----------------------------------------------')
'''
递归组成部分：递归调用 + 递归终止条件
'''
#6的阶乘
def fun(i):
    if i == 1:
        return 1
    return i * fun(i - 1)

print(fun(6))   #720


#斐波那契数列 前两位数字只和为后一位
#计算第六项的值
def fib(i):
    if i==1 or i==2:
        return 1
    sum = fib(i - 1) + fib(i - 2)
    return sum

print(fib(6)) #8

#输出前六位的数值
for i in range(1,7):
    print(fib(i))




print('------------------------------------------异常处理机制-----------------------------------------------')
# try:
#     a = int(input('请输入第一个整数：'))
#     b = int(input('请输入第二个整数：'))
#     result = a / b
#     print("a除b的结果是：",result)
# except ZeroDivisionError:
#     print('除数不允许为0')
# print('程序结束')


'''
多种类型的异常：
    按照先子类后父类的顺序(先捕获小的)
    为了避免可能遗漏的异常 在最后加一个BaseException
'''
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
    print("a除b的结果是：",result)
except ZeroDivisionError:
    print('除数不允许为0')
except ValueError:
    print('只能输入数字')
except BaseException as e:
    print(e)
print('程序结束')


'''
try...except...else结构
    try代码块未出现异常-->执行else代码块
    try代码块出现异常-->执行Except代码块
'''
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as e:
    print('出错了',e)
else:
    print("a除b的结果是：", result)
print('程序结束')



'''
try...except...else...finally结构
    无论是否发生异常 finally代码块始终会被执行 （通常用来释放try块中申请的资源）
    try代码块未出现异常-->执行else、finally代码块
    try代码块出现异常-->执行Except、finally代码块
'''
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as e:
    print('出错了',e)
else:
    print("a除b的结果是：", result)
finally:
    print('程序结束,谢谢您的使用')



'''
traceback模块打印异常信息 
'''
import traceback
try:
#    print(10/0)
    pass
except:
    traceback.print_exc()   #ZeroDivisionError: division by zero