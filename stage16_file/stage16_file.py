#encoding=gbk
print('---------------------------------------�ļ�����---------------------------------------------------')
'''
�����ı����ʽ��
python�Ľ�����ʹ�õ���Unicode(�ڴ�) -�������� 2���ֽڱ�ʾ1���ַ�
.py�ļ��ڴ�����ʹ��UTF-8�洢(���) -�䳤���� 1-4���ֽڱ�ʾ1���ַ� Ӣ��1���ֽ� ����3���ֽ�  UTF-8��Unicode��ʵ��
'''

#�޸��ļ��ı����ʽ
# .py�ļ����Ϸ� #encoding=gbk


print('---------------------------------------�ļ���д---------------------------------------------------')
'''
�ļ��Ķ�д��IO����
���ú���open()�����ļ�����
file = open(filename [,mode,encoding])   filename:Ҫ������򿪵��ļ�����  mode:�򿪷�ʽĬ��Ϊֻ��  encoding:Ĭ���ı��ļ����ַ��ı���Ϊgbk
'''
file = open('a.txt','r')
print(file.readlines())     #['�й�\n', '����']   ��ȡ���Ϊ�б�
file.close()



print('---------------------------------------���õ��ļ���ģʽ---------------------------------------------------')
'''
�ļ�������-�����ࣺ
    �ı��ļ����洢������ͨ���ַ����ı� Ĭ��unicode�ַ��� �����ü��±������
    �������ļ������������ԡ��ֽڡ���ʽ�洢 �޷��ü��±��� ��ʹ��ר�ŵ������ eg:MP3��Ƶ�ļ���jpg�ļ���doc�ĵ���
��ģʽ��
    r����ֻ��ģʽ���ļ� �ļ���ָ������ļ���ͷ
    w����ֻдģʽ���ļ� ����ļ��������򴴽� �ļ������򸲸�ԭ������ �ļ�ָ�����ļ��Ŀ�ͷ
    a����׷��ģʽ���ļ� ����ļ��������򴴽� �ļ�ָ�����ļ��Ŀ�ͷ  ����ļ����������ļ�ĩβ׷������ �ļ�ָ����ԭ�ļ�ĩβ
    b���Զ����Ʒ�ʽ���ļ� ���ܵ���ʹ�� ��Ҫ������ģʽһ��ʹ�� rb��wb
    +���Զ�д��ʽ���ļ� ���ܵ���ʹ�� ��Ҫ������ģʽһ��ʹ�� a+
'''
#w
file = open('b.txt','w')
file.write('helloworld')    #�½�b.txt�ļ� д��helloworld
file.close()

file = open('b.txt','w')
file.write('python')    #�޸�����b.txt�ļ� �滻ԭ������Ϊpython
file.close()

#a
file = open('b.txt','a')
file.write('Python')    #����b.txt�ļ� ׷������Python
file.close()

#rb  wb
src_file = open('dog.jpg','rb')
target_file = open('copyDog.jpg','wb')
target_file.write(src_file.read())
src_file.close()
target_file.close()



print('--------------------------------------------�ļ�����ĳ��÷���----------------------------------------')
'''
read([size]): ���ļ��ж�ȡsize���ֽڻ��ַ������ݷ��� ʡ��[size]���ȡ�ļ���������
readline()�����ı��ж�ȡһ������
readlines()�����ļ���ÿһ�ж���Ϊһ�������ַ������� �ŵ��б��з���
write(str)�����ַ���str����д���ļ�
writelines(s_list)�����ַ����б�s_listд���ı��ļ�������ӻ��з�
seek(offset[,whence])�����ļ�ָ���ƶ����µ�λ�� offset��Ϊ��->�����������ƶ� Ϊ��->����ʼ�����ƶ� whence��0->���ļ�ͷ��ʼ����(Ĭ��ֵ) 1->�ӵ�ǰλ�ÿ�ʼ���� 2->���ļ�β��ʼ����
tell()�������ļ�ָ��ĵ�ǰλ��
flush()���ѻ�����������д���ļ� �����ر��ļ�
close()���ѻ�����������д���ļ� ͬʱ�ر��ļ� �ͷ��ļ����������Դ
'''

#read()
file = open('a.txt','r')
print(file.read())      #���\n python
print(file.readline())  #���Ϊ��   ��һ�ζ�ȡ�� ����Ѿ���ĩβ ��Ҫ��seed()��ָ���ƶ�����ʼ
file.close()

#readline()
file = open('a.txt','r')
print(file.readline()) #���
file.close()

#readlines()
file = open('a.txt','r')
print(file.readlines()) #['���\n', 'python']
file.close()

# #write()
# file = open('a.txt','a')
# file.write('����write(2)')
# file.close()

# #writelines()
# file = open('a.txt','a')
# l1 = ['java','python']
# file.writelines(l1)
# file.close()

#seek()  tell()
file = open('b.txt','r')
file.seek(2)
print(file.read())  #thonPython  һ������ռ�����ֽ�/��ĸһ���ֽ�
print(file.tell())  #12 �����ļ�ָ�뵱ǰλ��
file.close()

# #flash()  close()
# file = open('c.txt','a')
# file.write('������ִ��flash')
# file.flush()        #flush����ر�ͨ��  python�ļ�->������->�����ļ�  flushָ���ǰѻ������ļ�д�����
# file.write('������ִ��close')
# file.close()



print('-------------------------------------�����Ĺ�����with���------------------------------------------')
'''
with����Զ�������������Դ ����ʲôԭ������with�� ����ȷ���ļ�����ȷ�ر� �Դ˴ﵽ�ͷ���Դ��Ŀ��
with open('�ļ���','����') as file:      open('�ļ���','����')��Ϊ�����ı��ʽ ���Ķ����Ϊ�����Ĺ�����
'''
with open('b.txt','r') as file:
    print(file.read())              #����дclose��� ֻҪ�뿪with����� �ͻ�ر��ļ�

#�����Ĺ�������ԭ��
#MyContentMgrʵ�������ⷽ��__enter__()�� __exit__(),����������������Ĺ�����Э�飬��ô�����ʵ�������Ϊ�������Ĺ�����
class MyContentMgr(object):
    def __enter__(self):
        print('enter����������ִ����')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit����������ִ����')

    def show(self):
        print('show����������ִ����')

with MyContentMgr() as mc:
    mc.show()       #�������enter��show��exit����������ִ��  show�������� ��Ȼ��ִ��exit����


#with���ʵ���ļ�����
with open('dog.jpg','rb') as src_file:
    with open('withCopyDog.jpg','wb') as target_file:
        target_file.write(src_file.read())