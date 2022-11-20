#-----------input()函数------------
# age = input('你今年几岁了？') #input函数是一个输入函数 函数结果为str类型  ’=‘将用户输入的内容赋值给age
# print(age,type(age))
# #从键盘录入两个整数 计算之和
# a=int(input('请输入一个加数：')) #input函数的输出为str类型 故要用int()函数先转为整型 再相加
# b=int(input('请输入另一个加数：'))
# print(a+b)


#------------python算数运算符---------------
print(1+2)
print(1-2)
print(1*1)
print(11/2) #5.5 --除法运算
print(11//2) #5 --整除运算
print(11%2) #1 --取余运算
print(2**2) #4 --2的2次方
print(2**3) #8 --2的3次方

# //一正一负整除 向下取整
print(-9//4) #-3 商为-2 向下取整为-3
print(9//-4) #-3 同上

# & 一正一负取余 余数=被除数-除数*商
print(9%-4) #-3 -- 结果为：9-（-4*（-3））=-3
print(-9%4) #3


#------------------python赋值运算符-----------------------
#运算顺序 从右到左
a=3+4
print(a) # 7
#链式赋值
a=b=c=20
print(a,id(a),b,id(b),c,id(c)) #a b c的id值一样

#参数赋值
a=20
a+=30 #50  a=a+30
print(a,type(a))
a-=30 #20 a=a-30=50-30
print(a,type(a))
a*=2 #40 a=a*2
print(a,type(a))
a/=3 #13.3.. a=a/3
print(a,type(a)) # 此时a变为float类型
a//=3 #4.0  a=a//3=13.3..//3
print(a,type(a))
a%=3 #1.0 a=a%3=4.0%3
print(a,type(a))

#系列解包赋值(左右两侧个数需一致)
a,b,c=10,20,30
print(a,b,c)
#a,b,c=10,20 #报错 左右个数不对应
#应用 交换两个变量时不需要中间变量 如下
a,b=10,20
print('交换前',a,b)
a,b=b,a
print('交换后',a,b)


#---------------python比较运算符------------------
a,b=10,20
print('a>b吗？',a>b) #Flase
print('a<b吗？',a<b)
print('a>=b吗？',a>=b)
print('a<=b吗？',a<=b)
print('a==b吗？',a==b)
print('a!=b吗？',a!=b)
#一个对象由三部分组成 标识、类型、值
# 一个= 赋值运算符、两个== 比较运算符(比较的是value)
a,b=10,10
print(a==b) #True # ==比较的是value
print(a is b)#False # is 比较的是标识(id)
list1=[11,22,33,44]
list2=[11,22,33,44]
print(list1==list2) #True 比较的是值value
print(list1 is list2) #Flase 比较的是标识id
print(list1 is not list2)#True list1和list2的id不相等


#---------------python布尔运算符------------------
a,b=1,2
print("----and 并且-----")
print(a==1 and b==2) #True  True and True -> True
print(a==1 and b<2) #Flase  True and Flase -> Flase
print(a!=1 and b==2) #Flase  Flase and True -> Flase
print(a!=1 and b!=2) #Flase  Flase and Flase -> Flase

print('----or 或者------')
print(a==1 or b==2) #True  True or True -> True
print(a==1 or b<2) #True  True or Flase -> True
print(a!=1 or b==2) #True  Flase or True -> True
print(a!=1 or b!=2) #Flase  Flase or Flase -> Flase

print('---not 对布尔类型操作数取反---')
f1=True
f2=False
print(not f1) #Flase
print(not f2) #True

print('----in 和 not in------')
s='helloworld'
print('w' in s) #True
print('k' in s) #Flase
print('w' not in s) #Flase
print('k' not in s) #True


#---------------python位运算符(将数据转为二进制进行计算)------------------
print(4&8) #按位与：将两个数字转为二进制，同为1得1，其中一个为0得0
print(4|8) #按位或：将两个数字转为二进制，其中一个为1得1 都为0得0
print(4<<1) #向左移位：将数字转为二进制，向左移动1位 相当于乘2
print(4<<2) #向左移位：将数字转为二进制，向左移动2位 相当于乘4
print(4>>1) #向右移位：将数字转为二进制，向右移动1位 相当于除2
print(4>>2) #向右移位：将数字转为二进制，向右移动2位 相当于除4


#---------------python运算符的优先级-------------------
# 括号() > 算术运算符(** * / // %  + - ) > 位运算符(<<  >>  & |) > 比较运算符(> < >= <= == !=) > 布尔运算符(and or) > 赋值运算符(=)
