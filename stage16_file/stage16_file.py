#encoding=gbk
print('---------------------------------------文件编码---------------------------------------------------')
'''
常见的编码格式：
python的解释器使用的是Unicode(内存) -定长编码 2个字节表示1个字符
.py文件在磁盘上使用UTF-8存储(外存) -变长编码 1-4个字节表示1个字符 英文1个字节 汉字3个字节  UTF-8是Unicode的实现
'''

#修改文件的编码格式
# .py文件最上方 #encoding=gbk


print('---------------------------------------文件读写---------------------------------------------------')
'''
文件的读写：IO操作
内置函数open()创建文件对象
file = open(filename [,mode,encoding])   filename:要创建或打开的文件名称  mode:打开方式默认为只读  encoding:默认文本文件中字符的编码为gbk
'''
file = open('a.txt','r')
print(file.readlines())     #['中国\n', '美丽']   读取结果为列表
file.close()



print('---------------------------------------常用的文件打开模式---------------------------------------------------')
'''
文件的类型-两大类：
    文本文件：存储的是普通‘字符’文本 默认unicode字符集 可以用记事本程序打开
    二进制文件：数据内容以‘字节’形式存储 无法用记事本打开 需使用专门的软件打开 eg:MP3音频文件，jpg文件，doc文档等
打开模式：
    r：以只读模式打开文件 文件的指针放在文件开头
    w：以只写模式打开文件 如果文件不存在则创建 文件存在则覆盖原有内容 文件指针在文件的开头
    a：以追加模式打开文件 如果文件不存在则创建 文件指针在文件的开头  如果文件存在则在文件末尾追加内容 文件指针在原文件末尾
    b：以二进制方式打开文件 不能单独使用 需要与其它模式一起使用 rb或wb
    +：以读写方式打开文件 不能单独使用 需要与其他模式一起使用 a+
'''
#w
file = open('b.txt','w')
file.write('helloworld')    #新建b.txt文件 写入helloworld
file.close()

file = open('b.txt','w')
file.write('python')    #修改已有b.txt文件 替换原有内容为python
file.close()

#a
file = open('b.txt','a')
file.write('Python')    #已有b.txt文件 追加内容Python
file.close()

#rb  wb
src_file = open('dog.jpg','rb')
target_file = open('copyDog.jpg','wb')
target_file.write(src_file.read())
src_file.close()
target_file.close()



print('--------------------------------------------文件对象的常用方法----------------------------------------')
'''
read([size]): 从文件中读取size个字节或字符的内容返回 省略[size]则读取文件所有内容
readline()：从文本中读取一行内容
readlines()：把文件中每一行都作为一个独立字符串对象 放到列表中返回
write(str)：将字符串str内容写入文件
writelines(s_list)：将字符串列表s_list写入文本文件，不添加换行符
seek(offset[,whence])：把文件指针移动到新的位置 offset：为正->往结束方向移动 为负->往开始方向移动 whence：0->从文件头开始计算(默认值) 1->从当前位置开始计算 2->从文件尾开始计算
tell()：返回文件指针的当前位置
flush()：把缓冲区的内容写入文件 但不关闭文件
close()：把缓冲区的内容写入文件 同时关闭文件 释放文件对象相关资源
'''

#read()
file = open('a.txt','r')
print(file.read())      #你好\n python
print(file.readline())  #输出为空   第一次读取完 光标已经在末尾 需要用seed()将指针移动回起始
file.close()

#readline()
file = open('a.txt','r')
print(file.readline()) #你好
file.close()

#readlines()
file = open('a.txt','r')
print(file.readlines()) #['你好\n', 'python']
file.close()

# #write()
# file = open('a.txt','a')
# file.write('我是write(2)')
# file.close()

# #writelines()
# file = open('a.txt','a')
# l1 = ['java','python']
# file.writelines(l1)
# file.close()

#seek()  tell()
file = open('b.txt','r')
file.seek(2)
print(file.read())  #thonPython  一个中文占两个字节/字母一个字节
print(file.tell())  #12 返回文件指针当前位置
file.close()

# #flash()  close()
# file = open('c.txt','a')
# file.write('接下来执行flash')
# file.flush()        #flush不会关闭通道  python文件->缓冲区->磁盘文件  flush指的是把缓冲区文件写入磁盘
# file.write('接下来执行close')
# file.close()



print('-------------------------------------上下文管理器with语句------------------------------------------')
'''
with语句自动管理上下文资源 不论什么原因跳出with块 都能确保文件的正确关闭 以此达到释放资源的目的
with open('文件名','操作') as file:      open('文件名','操作')称为上下文表达式 它的对象就为上下文管理器
'''
with open('b.txt','r') as file:
    print(file.read())              #不用写close语句 只要离开with代码块 就会关闭文件

#上下文管理器的原理
#MyContentMgr实现了特殊方法__enter__()、 __exit__(),则该类遵守了上下文管理器协议，那么该类的实例对象称为：上下文管理器
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了')

with MyContentMgr() as mc:
    mc.show()       #依次输出enter、show、exit方法被调用执行  show方法报错 依然会执行exit方法


#with语句实现文件复制
with open('dog.jpg','rb') as src_file:
    with open('withCopyDog.jpg','wb') as target_file:
        target_file.write(src_file.read())