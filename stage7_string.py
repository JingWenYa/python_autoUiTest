print('-------------------------------字符串的驻留机制---------------------------------------')
a = 'python'
b = "python"
c = '''python'''
print(a, id(a))  # python 1898774413552
print(b, id(b))  # python 1898774413552
print(c, id(c))  # python 1898774413552

# 驻留机制的前提
# 1、字符串的长度为0或者1时
a = '%'
b = '%'
print(a is b)  # True

# 2、符合标识符的字符串 (字母(汉字)、数字、下划线）
a = 'ab%'
b = 'ab%'
print(a is b)  # False

# 3、字符串只在编译时停留 而非运行时
a = 'abc'
b = 'ab' + 'c'  # 运行之前就拼接了
c = ''.join(['ab', 'c'])  # 运行时才会拼接
print(a is c)  # False
print(c)  # abc

# 4、[-5,256]之间的数字
a = -6
b = -6
print(a is b)  # False

# pycharm工具会强制驻留 需要在python编辑器中操作
# sys中的intern方法会强制2个字符串指向同一个对象
import sys

# a=sys.intern(b)
# print(a is b) #True

# 字符串拼接时建议用join方法，而非‘+’，join()会提前计算字符的长度然后拷贝，只new一次对象，效率比‘+’高


print('-------------------------------字符串的查询-----------------------------------------')
# index() 查找子串substr第一次出现的位置 不存在抛异常ValueError
s = 'hello,hello'
print(s.index('lo'))  # 3
# print(s.index('kl')) #报错

# rindex() 查找子串substr最后一次出现的位置 不存在抛异常ValueError
print(s.rindex('lo'))  # 9
# print(s.rindex('kl')) #报错

# find() 查找子串substr第一次出现的位置 不存在返回-1
print(s.find('lo'))  # 3
print(s.find('kl'))  # -1

# rfind() 查找子串substr最后一次出现的位置 不存在返回-1
print(s.rfind('lo'))  # 9
print(s.rfind('kl'))  # -1

#查询值
#方式一：[]
s = 'hello,hello'
print(s[1]) #e
print(s[0:5:2]) #hl0

#字符串的重复输出
print(s*2) #hello,hellohello,hello

#in   not in
print('p' in s) #False
print('a' not in s) #True

#len()
print(len(s)) #11


print('-------------------------------字符串的大小写转换（均会产生新的字符串对象）-----------------------------------------')
s1 = 'hello,python'

# upper() 全部字母转大写
s2 = s1.upper()  # 转成大写 产生新的字符串对象
print(s2, id(s1), id(s2))  # HELLO,PYTHON 2238970234160 2238970235312

# lower() 全部字母转小写
s2 = s1.lower()  # 转成小写 产生新的字符串对象
print(s2, id(s1), id(s2))  # hello,python 2238970234160 2238970235440

# swapcase() 所有大写字母转小写 所有小写字母转大写
s1 = 'hello,Python'
s2 = s1.swapcase()  # 产生新的字符串对象
print(s2, id(s1), id(s2))  # HELLO,pYTHON 2238970234160 2238970235376
# capitalize() 第一个字母转大写 其他转小写

# title() 每个单词的第一个字母转大写 每个单词的剩余字母转小写
s2 = s1.title()
print(s2, id(s1), id(s2))  # Hello,Python

print('----------------------------------字符串内容对齐----------------------------------------------')
s1 = 'hello,python'
# center() 居中对齐 第一个参数：指定宽度；第二个参数：指定填充符、可选、默认空格；设置宽度小于原宽度，返回原字符串
print(s1.center(20, '*'))  # ****hello,python****  对原字符串无改变

# ljust() 左对齐 第一个参数：指定宽度；第二个参数：指定填充符、可选、默认空格；设置宽度小于原宽度，返回原字符串
print(s1.ljust(20, '*'))  # hello,python********
print(s1.ljust(10, '*'))  # hello,python
print(s1.ljust(20))  # hello,python

# rjust() 右对齐 第一个参数：指定宽度；第二个参数：指定填充符、可选、默认空格；设置宽度小于原宽度，返回原字符串
print(s1.rjust(20, '*'))  # ********hello,python
print(s1.rjust(10, '*'))  # hello,python
print(s1.rjust(20))  # hello,python

# zfill() 右对齐 左边用0填充 该方法只接收一个参数 用于指定字符串宽度 设置宽度小于等于原宽度，返回原字符串
print(s1.zfill(20))  # 00000000hello,python
print(s1.zfill(10))  # hello,python
print('-1123'.zfill(10))  # -000001123

print('-------------------------------字符串内容劈分-------------------------------------------')

# split() 从左侧开始劈分 默认的劈分字符是空格字符串 返回是列表 / 可通过参数sep设置劈分符 / 通过参数maxsplit指定劈分最大次数 最大劈分后剩余的字串会单独做一部分
s = 'hello world python'
l1 = s.split()
print(l1)  # ['hello', 'world', 'python']
s1 = 'hello|world|python'
print(s1.split(sep='|'))  # ['hello', 'world', 'python']
print(s1.split())  # ['hello|world|python']
print(s1.split(sep='|', maxsplit=1))  # ['hello', 'world|python']

# rsplit() 从右侧开始劈分 默认的劈分字符是空格字符串 返回是列表 / 可通过参数sep设置劈分符 / 通过参数maxsplit指定劈分最大次数 最大劈分后剩余的字串会单独做一部分
print(s.rsplit())  # ['hello', 'world', 'python']
print(s1.rsplit(sep='|'))  # ['hello', 'world', 'python']
print(s1.rsplit(sep='|', maxsplit=1))  # ['hello|world', 'python']

#strip() 移除字符串头尾指定的字符（默认为空格或换行符）
s='00000000ha0123ha0000000000'
print(s.strip('0')) #ha123ha
s='  1 2 3  '
print(s.strip(' ')) #1 2 3
print(s.strip()) #1 2 3



print('-------------------------------字符串的常用判断方法-------------------------------------------')
# isidentifier() 判断指定字符串是不是合法的标识符
print('hello,pyhton'.isidentifier())  # False
print('hello'.isidentifier())  # True
print('张三_'.isidentifier())  # True
print('张三_123'.isidentifier())  # True

# isspace() 判断指定字符串是不是全由空白字符组成(回车、换行、水平制表)
print('\t'.isspace())  # True

# isalpha() 判断指定的字符串是不是全由字母组成
print('abc'.isalpha())  # True
print('张三'.isalpha())  # True
print('张三1'.isalpha())  # False

# isdecimal() 判断指定字符串是否全由十进制数字组成
print('123'.isdecimal())  # True
print('123四'.isdecimal())  # False
print('Ⅲ'.isdecimal())  # False

# isnumeric() 判断指定字符串是否全部由数字组成
print('123'.isnumeric())  # True
print('12a'.isnumeric())  # False
print('Ⅲ'.isnumeric())  # True

# isalnum() 判断指定字符串是否全由字母和数字组成
print('abc123'.isalnum())  # True
print('张三123'.isalnum())  # True
print('123!'.isalnum())  # False

print('---------------------------------字符串的替换和连接---------------------------------------------')
# replace() 字符串替换 第一个参数：被替换的子串；第二个参数：用来替换的子串；第三个参数：指定最大替换次数；该方法返回替换后得到的字符串，替换前的字符串不发生变化
s = 'hello,python'
print(s.replace('python', 'java'))  # hello,java
s1 = 'hello,python,python,python'
print(s1.replace('python', 'java', 2))  # hello,java,java,python

# join() 将列表或元组中的字符串合并成一个字符串
l1 = ['hello', 'world', 'python']
print(' '.join(l1))  # hello world python 用空格将列表元素连接
print('|'.join(l1))  # hello|world|python 用|将列表元素连接

t = ('hello', 'world', 'python')
print(' '.join(t))  # hello world python

print('*'.join('python'))  # p*y*t*h*o*n

print('-----------------------------------字符串的比较------------------------------------------------')
# 运算符> >= < <= == !=
# 比较规则：比较第一个字符 相等则继续比较下一个，直到不相等时，其比较结果即为两个字符串的比较结果
# 比较原理：字符比较时 比较的是原始值，调用内置函数ord可以得到原始值；与其相反的函数内置函数chr，根据原始值得到对应的字符
print('apple' > 'app')  # True
print('apple' > 'banana')  # False 97>98错误
print(ord('a'), ord('b'))  # 97 98
print(ord('郭'))  # 37101
print(chr(37101))  # 郭

'''is和==的区别 is比较的是内存地址id  ==比较的是值'''
a = b = 'python'
c = 'python'
print(a == b, b == c)  # True True
print(a is b, b is c)  # True True

print('-----------------------------------字符串的切片------------------------------------------------')
# 字符串是不可变序列 不具备增删改操作 切片将产生新的对象
s = 'hello,python'
s1 = s[:5]  # hello
s2 = s[6:]  # python
s3 = '!'
newstr = s1 + s3 + s2
print(newstr)  # hello!python
print(id(s1), id(s2), id(s3), id(newstr))  # 2193990718960 2193990718768 2193990716848 2193990718896

print("--切片详解(与列表一致)--")
print(s[1:5:1])  # ello 从1开始，到5结束(不包含5)，步长为1
print(s[::2])  # hlopto 默认从0开始，到最后一个字符，步长为2
print(s[::-1])  # nohtyp,olleh 索引为负数->默认从最后一个元素开始,到第一个元素结束
print(s[-6::1])  # python 从索引-6开始，到最后一个元素结束

print('-----------------------------------字符串的格式化------------------------------------------------')
# 方法一：%作为占位符 %s表示字符串 %i或者%d作为整数  %f作为浮点数
name = '张三'
age = 20
print('我叫%s,今年%d岁' % (name, age))

# 宽度
print('%10d' % 99)  # 99 10表示总宽度
# 精度
print('%.3f' % 3.1415926)  # 3.142 .3表示小数点后几位
# 精度+宽度
print('%10.3f' % 3.1415926)  # 总宽度为10 小数点后3位
print('%10d,%10.3f' % (99, 31111.1415926))  # 99, 31111.142

# 方法二：{}作为占位符 使用.format()方法
print('我叫{0},今年{1}岁'.format(name, age))  # 0和1代表替换值的顺序

# 宽度和精度
print('{0}'.format(3.1415926))  # 3.1415926
print('{0:.3}'.format(3.1415926))  # 3.14    .3表示一共三位数
print('{0:.3f}'.format(3.1415926))  # 3.142   .3f表示一共三位小数
print('{0:10.3f}'.format(3.1415926))  # 3.142   同时设置宽度和精度 一共十位，3位小数
print('{:10.3f}'.format(3.1415926))  # 3.142   同上 只有一位时可以省略不写

# 方法三：f
print(f'我叫{name},今年{age}岁')  # 我叫张三,今年20岁

print('-----------------------------------字符串的编码转换------------------------------------------------')
# 为什么需要字符串的编码转换->计算机之间要通过byte字节传输
# 编解码方式：编码-->encode()方法 将字符串转为二进制     解码-->decode()方法 将bytes类型数据转为字符串
# 编码
s = '本来无一物'
print(s.encode(encoding="GBK"))  # GBK编码格式 一个中文占两个字节  b'\xb1\xbe\xc0\xb4\xce\xde\xd2\xbb\xce\xef'
print(s.encode(encoding="UTF-8"))  # GBK编码格式 一个中文占三个字节  b'\xe6\x9c\xac\xe6\x9d\xa5\xe6\x97\xa0\xe4\xb8\x80\xe7\x89\xa9'

# 解码
byte = s.encode(encoding="GBK")
print(byte.decode(encoding="GBK"))  # 本来无一物
# print(byte.decode(encoding="UTF-8")) #报错 编解码方式不一致

byte = s.encode(encoding="UTF-8")
print(byte.decode(encoding="UTF-8"))  # 本来无一物
