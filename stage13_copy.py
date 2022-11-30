print('----------------------------------------变量的赋值操作-----------------------------------------------')
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu1 = CPU()
#变量的赋值
cpu2 = cpu1
print(cpu1,id(cpu1))    #1659926014344
print(cpu2,id(cpu2))    #1659926014344


print('---------------------------------------------浅拷贝----------------------------------------------------')
'''
python中无特殊说明都是浅拷贝
拷贝时 对象包含的子对象内容不拷贝 -->源对象与拷贝对象会引用同一个子对象
'''
disk = Disk()
computer = Computer(cpu1,disk)

#浅拷贝
import copy
computer2 = copy.copy(computer)
print(computer,computer.disk,computer.cpu)      #0x000001F61EEF1C88 0x000001F61EEF1D48  0x000001F61EEF1B48
print(computer2,computer2.disk,computer2.cpu)   #0x000001F61EEF1E08 0x000001F61EEF1D48  0x000001F61EEF1B48


print('---------------------------------------------深拷贝----------------------------------------------------')
'''
使用的是copy模块的deepcopy函数 
递归拷贝对象中包含的子对象 -->源对象和拷贝对象所有的子对象也不相同
'''
computer3 = copy.deepcopy(computer)
print(computer,computer.disk,computer.cpu)      #0x000001F61EEF1C88 0x000001F61EEF1D48  0x000001F61EEF1B48
print(computer3,computer3.disk,computer3.cpu)   #0x0000022CA69B3A08 0x0000022CA69BC308  0x0000022CA69BC1C8

a = 1
b=copy.deepcopy(a)
print(id(a),id(b))