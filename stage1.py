#coding:gbk
# ----------------�ַ�������-------------------
str1='������� ����python'
str2="������� ����python"
str3='''�������
����python'''
str4="""�������
����python"""
print(str1,type(str1))
print(str1,type(str2))
print(str1,type(str3))
print(str1,type(str4))

name='����'
age=20
#print('����'+name,'����'+age) #����ͬ���͵��ַ����á�+��ƴ�� �ᱨ�������������������ת��
print('����'+name,'����'+str(age))#��int����תΪstr���� str()

#---------------��������ת��--------------------
print('--str()����������תΪstr����--')
int1=10
float1=10.2
bool1=True
print(type(int1),type(float1),type(bool1))
print(type(str(int1)),type(str(float1)),type(str(bool1))) #���͡������͡������;���תΪ�ַ���

print('--int()����������תΪint����--')
str1='12'
str2='12.1'
str3='����'
float2=13.4
bool1=False
print(type(str1),int(str1)) #12 --��str����תΪint�� str������Ϊ�������ַ���
#print(type(str2),int(str2)) #���� str2�����������ַ���
#print(type(str3),int(str3)) #���� str2�����������ַ���
print(type(float2),int(float2)) #13 --��float����תΪint��  ���ȡfloat��С������
print(type(bool1),int(bool1)) #0 --��boolean����תΪint�� ��Ӧ1��0

print('--float()����������תΪ��������---')
str1='12'
str2='12.1'
str3='����'
int1=13
bool1=False
print(type(str1),float(str1)) #12.0 --��str����תΪfloat�� str������Ϊ����
print(type(str2),float(str2)) #12.1
#print(type(str3),float(str3)) #����
print(type(int1),float(int1)) #13.0
print(type(bool1),float(bool1)) #0.0

#---------------------pythonע��-----------------------------
#����
 #1������ע�� ��#
 #2�����ı�������ע�� �ļ���ͷ��� #coding:utf-8(python3Ĭ�ϸ�ʽ)��#coding:gbk
#����ע�� ��"""""",��''''''
"""���ǵ�һ��
���ǵڶ���
"""
















