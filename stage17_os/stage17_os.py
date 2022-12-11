print('--------------------------------------------文件操作------------------------------------------------')
'''
目录操作
  os是python内置的与操作系统功能和文件系统相关的模块 该模块语句的执行结果通常与操作系统有关 不同操作系统运行结果不同
os模块与os.path模块用于对目录或文件进行操作
'''
import os
#调用系统exe文件
#os.system('notepad.exe') #打开了记事本
#os.system('calc.exe') #打开了计算器
#调用
# os.startfile('C:\\Program Files (x86)\\Tencent\\QQ\\Bin\\QQ.exe')


print('--------------------------------------os模块 操作目录相关函数--------------------------------------------')
'''
getcwd(): 返回当前的工作目录
listdir(path): 返回指定路径下的文件和目录信息
mkdir(path[,mode]): 创建目录
makedirs(path1/path2...[,mode]): 创建多级目录
rmdir(path): 删除目录
removedirs(path1/path2...): 删除多级目录
chdir(path): 将path设置为当前工作目录
'''
#获取当前工作目录
print(os.getcwd())  #C:\Case_Depository\pythonProject\stage17_os
#返回指定路径下的文件和目录信息
print(os.listdir('../stage17_os'))
#创建目录
# os.mkdir('newdir')
#创建多级目录
# os.makedirs('a/b/c')
#删除目录
# os.rmdir('newdir')
#删除多级目录
# os.removedirs('a/b/c')
#将path设置为当前工作目录
# os.chdir('C:\Case_Depository\pythonProject\stage16_file')
# print(os.getcwd())  #C:\Case_Depository\pythonProject\stage16_file



print('--------------------------------------os.path模块 操作目录相关函数------------------------------------------')
'''
abspath(path): 获取文件或目录的绝对路径
exists(path): 判断文件或目录是否存在 存在->返回true  不存在->返回false
join(path,name): 将目录与目录或文件名拼接起来
splitext(): 分离目录名与文件名
splitext(): 分离文件名与扩展名
basename(path): 从一个目录中提取文件名
dirname(path): 从一个路径中提取文件路径 不包括文件名
isdir(path): 判断是否为路径
'''
import os.path as path
#获取文件或目录的绝对路径
print(path.abspath('stage17_os.py'))    #C:\Case_Depository\pythonProject\stage17_os\stage17_os.py
#判断文件或目录是否存在
print(path.exists('stage17_os.py'),path.exists('stage100_os.py'))   #True False
#将目录与目录或文件名拼接起来
print(path.join('C:\\Users\\MeetYou\\Desktop\\test','stage17_os.py'))   #C:\Users\MeetYou\Desktop\test\stage17_os.py
#分离目录名与文件名
print(path.split('C:\\Users\\MeetYou\\Desktop\\test\\stage17_os.py'))   #('C:\\Users\\MeetYou\\Desktop\\test', 'stage17_os.py')
#分离文件名与扩展名
print(path.splitext('stage17_os.py'))   #('stage17_os', '.py')
#目录中提取文件名
print(path.basename('C:\\Users\\MeetYou\\Desktop\\test\\stage17_os.py'))    #stage17_os.py
#路径中提取文件路径
print(path.dirname('C:\\Users\\MeetYou\\Desktop\\test\\stage17_os.py'))     #C:\Users\MeetYou\Desktop\test
#判断是否为路径
print(path.isdir('C:\\Users\\MeetYou\\Desktop\\test\\stage17_os.py'))       #False


print('---------------------------------------列出指定目录下的所有.py文件-------------------------------------------')
import os
path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)


print('------------------------------------walk: 递归遍历指定目录下的所有文件---------------------------------------')
import os.path
path = os.getcwd()
list_files = os.walk(path)
for dirpath,dirname,filename in list_files:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print('----------------------------')

    for dir in dirname:
        print(os.path.join(dirpath,dir))        #join方法不会改变原有原字符串id值
    for file in filename:
        print(os.path.join(dirpath,file))
    print('---------------------------------')

s = 'abc'
print(id(s))
print(s.join('snf'))
print(id(s))