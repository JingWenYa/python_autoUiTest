#列表
a=10 #变量存储的是单个对象的引用
l1=['hello','world',123] #列表存储的是一组对象的引用
print(id(list))
print(type(list))
print(list)


print('-----------------------列表的创建--------------------------------')
#第一种方式 使用方括号[]
l1=['hello','world',123]
print(l1)
#第二种方式 使用list()函数
l2=list(['hello1','world1',123])
print(l2)


print('-----------------------列表的特点---------------------------------')
#1、列表元素有序
#2、列表索引定位唯一数据l1[0]、l1[1]  从左往右 索引从0开始  从右往左 索引从-1开始
#3、列表可以存储重复数据
l2=list(['hello1','world1',123,'hello1'])
#4、任意数据类型混存
#5、根据需要动态分配和回收内存 不用定义列表大小


print('--------------------------列表元素的查询-------------------------------')
print('获取列表中指定元素的索引(index()方法)')
l1=['hello','world',123,'hello']
print(l1.index('hello')) #列表中存在多个相同元素 只返回相同元素的第一个索引
#print(l1.index('python')) #查询元素不存在 报错ValueError
#print(l1.index('hello',1,3)) #左闭右开 在'world',123范围内查找 报错ValueError
print(l1.index('hello',1,4)) #3

print('-获取列表中指定索引的元素值-')
l1=['hello','world',123,'hello','world',456]
print(l1[1]) #world 获取索引为1的元素
print(l1[-4]) #123 获取索引为-4的元素 从右往左-1、-2、-3、-4、-5、-6
#print(l1[10]) #报错 超出范围

print('获取列表中的多个元素（切片）')
l1=[10,20,30,40,50,60,70,80]
#start=1,stop=6,step=1 左闭右开 切片后为新的列表
print(l1[1:6:1])
l2=l1[1:6:1]
print('原列表',id(l1))
print('切片后的列表',id(l2))
#---不写步长 默认步长为1---
print(l1[1:6])
print(l1[1:6:]) #默认步长为1

#start=1,stop=6,step=2 左闭右开 切片后为新的列表
print(l1[1:6:2]) #[20, 40, 60]
#---不写start，默认从头开始---
print(l1[:6:2]) #默认从0开始
#----不写stop，默认到最后----
print(l1[1::2]) #默认到最后

#-----step步长为负数-------
#步长为-1，头尾省略，逆向输出
print(l1[::-1]) #从尾到头 逆向输出
#步长为-1，strat=7，stop省略
print(l1[7::-1])
#步长为-2，strat=6，stop=0
print(l1[6:0:-2]) #[70, 50, 30]
print(l1[-1:-6:-2]) #[80, 60, 40]

print('判断指定元素是否在列表中存在')
#in   not in
l1=[10,20,'hello','python']
print(10 in l1) #True
print(100 in l1) #False
print(10 not in l1) #False
print(100 not in l1) #True

print('列表元素的遍历')
for item in l1:
    print(item)

#len()列表元素个数
print(len(l1)) #4

#max() 返回列表元素最大值
l1=[11,2,3,4,4]
print(max(l1)) #11

#min() 返回列表元素最小值
print(min(l1)) #2

#count() 统计某个元素在列表中出现的次数
print(l1.count(4)) #2



print('---------------------------列表元素的新增操作----------------------------')
#append() 在列表的末尾添加一个元素 不会创建新的列表
l1=[10,20]
l1.append('100')
print('添加之后', l1)

l2=['hello','world']
l1.append(l2) #[10, 20, '100', ['hello', 'world']] 将l2列表作为一个元素添加到l1的末尾
print(l1)

#extend() 在列表的末尾至少添加一个元素
l1=[10,20]
l1.extend(l2)
print(l1) #[10, 20, 'hello', 'world'] 将l2列表中的每一个元素 分别添加到l1的末尾

#insert() 在列表的任意位置上添加一个元素
l1.insert(1,90)
print(l1) #[10, 90, 20, 'hello', 'world']
l1.insert(1,l2)

#切片 在列表的任意位置至少添加一个元素
l1=['hello','world',123,'hello','world',456]
l2=[1,2,3]
l1[1:]=l2 #切片的开始和结束参数 表示要切掉的数据  用l2替代切掉的部分
print(l1) #['hello', 1, 2, 3]


print('---------------------------列表元素的删除操作-------------------------------')
#remove() 根据value移除一个元素 重复时只移除第一个 不存在时抛出valueError
l1=[10,20,30,40,50,60,30]
l1.remove(30)
print(l1) #[10, 20, 40, 50, 60, 30]

#pop() 根据索引移除一个元素  不指定索引时删除最后一个元素  指定索引不存在抛出inedxError
l1.pop(1)
print(l1) #[10, 40, 50, 60, 30]
#l1.pop(5) #报错
#不指定索引 移除最后一个元素
l1.pop()
print(l1) #[10, 40, 50, 60]

#切片 一次至少删除一个元素 将产生新的列表
l2=l1[1:3]
print(l2) #[40, 50]

#切片 不产生新的列表 而是删除原列表的内容
l1[1:3]=[]
print(l1) #[10, 60]

#删除列表的某个元素
del l1[1]
print(l1) #[10]

#clear() 清空列表
l1.clear()
print(l1) #[]

#del 删除列表
del l1
#print(l1) #l1 not defined



print('---------------------------列表元素的修改操作----------------------------------')
#一次修改一个值
l1=[10,20,30,40]
l1[2]=100
print(l1) #[10, 20, 100, 40]

#一次修改多个值
l1[1:3]=[300,400,500,600]
print(l1) #[10, 300, 400, 500, 600, 40]



print('---------------------------列表元素的排序操作----------------------------------')
#sort() 默认升序从小到大排序    指定reverse=True进行降序排序  在原列表基础上修改 不产生新列表
l1=[20,40,10,98,54]
l1.sort() #或 l1.sort(reverse=False)
print(l1) #升序
#指定reverse=True 进行降序排序
l1.sort(reverse=True)
print(l1) #降序

#内置函数sorted() 指定reverse=True 进行降序排序  产生一个新的列表 原列表不改变
l1=[20,40,10,98,54]
l2 = sorted(l1)
print(l2) #[10, 20, 40, 54, 98]
#指定reverse=True 进行降序排序
desc_list = sorted(l1,reverse=True)
print(desc_list) #[98, 54, 40, 20, 10]



print('---------------------------列表生成式----------------------------------')
l1 = [i for i in range(1,10)]
print(l1)
#生成一个2，4，6，8，10的列表
l2 = [i*2 for i in range(1,6)]
print(l2)