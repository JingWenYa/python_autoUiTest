#coding:gbk
# ----------------字符串类型-------------------
str1='人生苦短 我用python'
str2="人生苦短 我用python"
str3='''人生苦短
我用python'''
str4="""人生苦短
我用python"""
print(str1,type(str1))
print(str1,type(str2))
print(str1,type(str3))
print(str1,type(str4))

name='张三'
age=20
#print('姓名'+name,'年龄'+age) #将不同类型的字符串用‘+’拼接 会报错，解决方案：数据类型转换
print('姓名'+name,'年龄'+str(age))#将int类型转为str类型 str()

#---------------数据类型转换--------------------
print('--str()将其他类型转为str类型--')
int1=10
float1=10.2
bool1=True
print(type(int1),type(float1),type(bool1))
print(type(str(int1)),type(str(float1)),type(str(bool1))) #整型、浮点型、布尔型均可转为字符型

print('--int()将其他类型转为int类型--')
str1='12'
str2='12.1'
str3='哈哈'
float2=13.4
bool1=False
print(type(str1),int(str1)) #12 --将str类型转为int型 str类型需为整数的字符串
#print(type(str2),int(str2)) #报错 str2不是整数的字符串
#print(type(str3),int(str3)) #报错 str2不是整数的字符串
print(type(float2),int(float2)) #13 --将float类型转为int型  会截取float的小数部分
print(type(bool1),int(bool1)) #0 --将boolean类型转为int型 对应1和0

print('--float()将其他类型转为浮点类型---')
str1='12'
str2='12.1'
str3='哈哈'
int1=13
bool1=False
print(type(str1),float(str1)) #12.0 --将str类型转为float型 str类型需为数字
print(type(str2),float(str2)) #12.1
#print(type(str3),float(str3)) #报错
print(type(int1),float(int1)) #13.0
print(type(bool1),float(bool1)) #0.0

#---------------------python注释-----------------------------
#井号
 #1、单行注释 用#
 #2、中文编码声明注释 文件开头添加 #coding:utf-8(python3默认格式)、#coding:gbk
#多行注释 用"""""",或''''''
"""我是第一行
我是第二行
"""
















