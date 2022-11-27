"""
print
"""
#将数据写入文件中 （1、所指定盘符需存在 2、使用file=fp）
# fp=open('/Users/guojingwen/Desktop/text.txt','a+') #a+ 文件不存在就创建 存在就追加
fp=open('C:/Users/MeetYou/Desktop/test.txt','a+')
print('helloword',file=fp)
fp.close()
#不换行输出
print('hello','word','python')

"""
换行符
"""
#换行
print('hello\nworld') # \n = newline
#制表符
print('hello\tworld') #hello	world
print('hellooo\tworld') #hellooo world
#退格符
print('hello\bworld')#将上一个字符覆盖 b=back
#回车符
print('hello\rworld')#回到第一个字符 hello被完全覆盖  r=return
#\转义字符
print('http:\\www.baidu.com') #输出结果为http:\www.baidu.com
print('http:\\\www.baidu.com')#输出结果为http:\\www.baidu.com
#原字符r  不希望字符串中的转移符起作用 在字符串前加r或R
print(r'hello\nworld')  #但末尾不能是反斜杠 会报错
print(r'hello\nworld\\') #加两个反斜杠即可
print(type(1))

"""
数据类型
"""
#整数 -正数、负数、0
n1=100
n2=-12
n3=0
type(n1)
#整数分为二进制、八进制、10进制、十六进制
print('十进制',10);
print('二进制',0b11) #二进制以0b开头
print('八进制',0o11764) #八进制以0o开头
print('十六进制',0xAF) #十六进制以0x开头

#浮点型
n4=1.1
n5=2.2
print(type(n4))
print(n4+n5)  #得到的值为3.3000000000000003
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#布尔类型(可以转成整型计算 与整型的1和0对应)
#True->1  False->0
f1=True
f2=False
print(type(f1))
print(f1+f2) #1+0