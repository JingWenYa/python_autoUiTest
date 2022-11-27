print('--------------------------------内置函数range() 用于生成一个整数序列---------------------------------------------')
# range()
# 优点：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都相同，因为仅需要存储start、stop和step；只有当用到range对象时，才会去计算序列中的相关元素
#方式一 range(stop) 生成从0到stop的整数
r=range(10)
print(r) #range(0, 10)
print(list(r)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#方式二 range(start,stop)
r=range(-3,5)
print(list(r)) #[-3, -2, -1, 0, 1, 2, 3, 4]

#方式三 range(start,stop,step)
r=range(-3,5,2)
print(list(r)) #[-3, -1, 1, 3]

#in   not in
print(10 not in r) #True
print(1 in r) #True




print('-------------------------------------where循环---------------------------------------------')
#循环判断N+1次，条件为true执行N次
#四步循环法：①初始化变量 ②条件判断 ③条件执行体(循环体) ④改变变量 --初始化变量 与条件判断变量 与改变变量为同一个
#计算1到4之间的和
sum=0
a=1
while a<5:
    sum+=a
    a+=1
print(sum)

#计算1到100之间的偶数和
sum = 0
a = 1
while a <= 100:
    if a % 2 == 0:
#    if not bool(a%2):    #方式二
        sum += a
    a += 1
print(sum)




print('''''''''''''''''''''''''''''''''''''for-in循环''''''''''''''''''''''''''''''''''''''''''')
# in表示从(字符串、序列等)中依次取值  for-in对象必须是可迭代对象
#for 自定义的变量 in 可迭代的对象：
#       循环体

#字符串是可迭代序列
for item in 'python':
    print(item)        #p y t h o n

#range()函数产生一个整数序列 也是可迭代对象
for item in range(5):
    print(item)

#如果在循环体中不需要用到自定义变量 可将自定义变量写为’_‘
for _ in range(5):
    print('人生苦短，我用python')

#计算1-100之间的偶数和
sum = 0
for item in range(1, 101):
    if item % 2 == 0:
        sum += item
print(sum)

#输出100到999之间的水仙花数
sum=0
for item in range(100, 1000):
     if (item // 100)**3 +(item // 10 % 10)**3+(item % 10)**3 == item:
         print(item)



print('-------------------------------------------流程控制语句break-----------------------------------------')
#用于结束跳出循环 通常与if语句搭配使用

#从键盘录入密码 最多输入三次 正确则结束循环
# for _ in range(3):
#     pwd = input("请输入密码：")
#     if pwd=='8888':
#         print('密码正确')
#         break
#     else:
#         print('密码错误')
#
# #while循环实现
# i = 1
# while i <=3:
#     pwd = input("请输入密码：")
#     if pwd=='8888':
#         print('密码正确')
#         break
#     else:
#         print('密码错误')
#         i+=1

#二层循环中的break，用于控制本层循环



print('------------------------------------------------流程控制语句continue------------------------------------------')
#用于结束当前循环 进入下一次循环 通常与if语句搭配使用

#输入1到50之间所有5的倍数 使用continue实现
for i in range(1,51):
    if i % 5 != 0:
        continue
    print(i)

#二层循环中的continue，用于控制本层循环



print('-------------------------------------------else语句-------------------------------------------------------')
#与else语句配置使用的三种情况
#① if...else...       if不满足时执行else
#② while...else...    没有碰到break时执行else
# i = 1
# while i <=3:
#     pwd = input("请输入密码：")
#     if pwd=='8888':
#         print('密码正确')
#         break
#     else:
#         print('密码错误')
#         i+=1
# else:
#     print('对不起，三次密码均输入错误')
#
# #③ for...else...      没有碰到break时执行else
# for _ in range(3):
#     pwd = input("请输入密码：")
#     if pwd=='8888':
#         print('密码正确')
#         break
#     else:
#         print('密码错误')
# else:
#     print('对不起，三次密码均输入错误')



print('----------------------------------------------嵌套循环-------------------------------------------------------')
#输出一个三行四列的矩形
for _ in range(3):
    for _ in range(4):
        print('*',end='\t') #不换行输出
    print('\n') #换行

#打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()


