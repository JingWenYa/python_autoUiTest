print('----------------------------------------模块的创建-----------------------------------------------------')
'''
优点：
一个.py文件就是一个模块
一个模块可以包含n个函数、类、变量等
优点：方便其他程序和脚本的导入并使用、避免函数名和变量名冲突、提高代码可维护性、提高代码可重用性
'''


print('-------------------------------------------模块的导入------------------------------------------------')
'''
导入模块方式：
1、import 模块名称 [as 别名]
2、from 模块名称 import 函数/变量/类
'''
import math
#查看math对象包含的方法
print(dir(math))
print(math.ceil(9.001))     #10
print(math.floor(9.999))    #9
print(math.pow(2,3))        #8.0  2的3次方
print(math.pi)              #3.141592653589793

#导入模块的某个方法
from math import pi
print(pi)

from math import ceil
print(ceil(2.89))



print("-----------------------------------------------自定义模块的导入----------------------------------------")
"""
将要导入.py模块所在的文件夹 右键->将目标设置为->源根
"""
import calc2
print(calc2.add(1, 3)) #4


print('----------------------------------------------以主程序的形式运行-------------------------------------------')
'''
if _name_=='_main_':
每个模块的定义中都包含记录模块名称的变量_name_，程序检查该变量以确认在哪个模块中运行，如果一个模块未被导入到其他程序中执行，那么它可能在解释器的顶级模块中执行，顶级模块的_name_变量值为_main_
'''
import calc2
print(calc2.add(1,5))  #6




print('----------------------------------------------常用的内置模块-------------------------------------------')
'''
sys：与python解释器及其环境操作相关的标准库
time：提供与时间相关的各种函数的标准库
os：提供了访问操作系统服务功能的标准库
calendar：提供与日期相关的各种函数的标准库
urllib：用于读取来自网上（服务器）的数据标准库
json：用于使用json序列化和反序列化对象
re：用于在字符串中执行正则表达式匹配和替换
math：提供标准算数运算函数的标准库
decimal：用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算
logging：提供了灵活的记录事件、错误、警告和调试信息等日志信息功能
random: 随机生成数字
'''

import sys
print(sys.getsizeof(48))    #28字节
print(sys.getsizeof(True))  #28字节
print(sys.getsizeof(False)) #24字节

import time
print(time.time())          #当前秒 1669895465.2481675
print(time.localtime())     #将秒转为具体的时间 tm_year=2022, tm_mon=12, tm_mday=1, tm_hour=19, tm_min=51, tm_sec=5, tm_wday=3, tm_yday=335, tm_isdst=0

import os
print(os.name)

import  urllib.request
print(urllib.request.urlopen('http://www.baidu.com/').read())

import random
print(random.random())  #0.8029786605615116 随机生成0到1之间的小数
print(random.randint(1,3))  #1 随机生成0到3之间的整数




print('------------------------------------------------第三方模块的安装和使用------------------------------------------')
'''
在win+r界面操作如下步骤：
pip install 模块名
输入python进入交互式应用程序 输入import 模块名  不报错即代表安装成功

第三方模块的安装：pip install 模块名
第三方模块的使用：import 模块名
'''

#pymysql
import pymysql

#request
import requests






# import schedule
# def job():
#     print('开开心心每一天')
#
# schedule.every(3).seconds.do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)















