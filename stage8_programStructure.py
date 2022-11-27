#python中一切皆对象 所有的对象都有布尔值
print('----------------布尔值为false的：False、数值0、None、空字符串、空列表、空元组、空字典、空集合,其他对象的布尔值均为true----------------')
print(bool(False)) #False
print(bool(0)) #False
print(bool(None)) #False
print(bool('')) #False
print(bool(' '))#True
print(bool([])) #False
print(bool(list())) #False
print(bool(())) #False
print(bool(tuple())) #False
print(bool({})) #False
print(bool(dict())) #False
print(bool({})) #False
print(bool(set())) #False

print(bool('123')) #True
print(bool(True)) #True


#用处
age=int(input("请输入年龄："))
if age:
    print(age)
else:
    print('年龄为:',age)



print('-----------------------------------------选择结构----------------------------------------------')
print('--单分支结构 if--')
money=1000
s=int(input("请输入取款金额："))
if money>=s:
    money=money-s
    print('取款成功，余额为', money)


print('--双分支结构 if else--')
num=int(input("请输入一个整数："))
if num%2==0:
    print(num,"是偶数")
else:
    print(num, "是奇数")

print("--双分支结构简写--")
print((num,"是偶数") if num%2==0 else (num, "是奇数"))
print(str(num)+"是偶数" if num%2==0 else str(num)+"是奇数")

print('-多分支结构 if elif elif [else:]  --else可不写-')
score=int(input("请输入成绩："))
if score>=90 and score<=100:  #或 90<=score<=100
    print('A级')
elif score>=80 and score<90:
    print('B级')
elif score>=70 and score<80:
    print('C级')
elif score>=60 and score<70:
    print('D级')
elif score<60:
    print('E级')
else:
    print('成绩有误，不在有效范围内')


print('-嵌套if-')
anwser=input("你是会员吗？y/n")
money=float(input("请输入您的购物金额："))
if anwser == 'y':
    if money >=200:
        print('打8折，付款金额为',money *0.8)
    elif money>=100:
        print('打9折，付款金额为', money * 0.9)
    else:
        print('不打折，付款金额为', money)
else:
    if money>=200:
        print('打9折，付款金额为', money * 0.95)
    else:
        print('不打折，付款金额为', money)



print('-----------------------------------------pass语句----------------------------------------------')
#pass:什么都不做，只是一个占位符
#使用场景：先搭建代码块 还没想好怎么写时
