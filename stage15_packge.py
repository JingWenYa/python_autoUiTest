print('-----------------------------------------------包的概念-----------------------------------------')
'''
包是一个分层次的目录结构，将一组功能相近的模块组织在一个目录下
作用：代码规范、避免合并冲突
包与目录的区别：包--> 包含__init__.py文件的目录称为包  目录中通常不包含__init__.py文件
包的导入：import 报名.模块名

设置为包：文件->右键->新建->python软件包
设置为目录：文件->右键->新建->目录
'''



print('-----------------------------------------------导入-----------------------------------------')
'''
使用import方式导入 后面只能跟包名 或模块名
使用from方式导入 后面可以跟包 模块名 函数名 变量名
'''
#import
import package.module_A
print(package.module_A.a)

#或者起别名
import package.module_A as ma       #ma为别名
print(ma.a)


#from
#模块
from package import module_A
from package.module_A import a
from calc2 import add
from math import pi
from math import *

