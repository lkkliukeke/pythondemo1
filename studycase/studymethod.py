#包裹位置传递
from functools import reduce


def master(*args):
    print(args)
master('zhangsan',18,'你好')
#包裹传递返回字典
def mast(**kwargs):
    print(kwargs)
mast(name='zhangsan',age='男')

#拆包
def Mas():
    return 100,200
mas1,mas2 = Mas()
print(mas1)
print(mas2)


#lambda表达式
fn1 = lambda a, b: a if a > b else b
print(fn1(1000, 500))

#lambda表达式
students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]
# 按name值升序排列
students.sort(key=lambda x: x['name'])
print(students)


#内置map函数
#map(fun1,lis),将传入的函数变量fun1 作用到lis变量的每个元素中，并将结果组成新的列表返回
lists = [1,2,3,4,5]
def fun1(x):
    return x**2
results = map(fun1,lists)
print(results)
print(list(results))

#内置reduce函数
#reduce(fun1,lis)，其中fun1中比醋鱼两个参数，每次fun1计算的结果继续和序列的下一个元素做累积计算
list1 = [1,3,5,7,9]
def fun2(a,b):
    return a+b
case = reduce(fun2,list1)
print(case)

#内置函数filter
#filter(fun1,lis),函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象，若需转换为列表，需用list()来转换
list2 = [2,5,6,7,8,10]
def fun3(x):
    return x % 2 == 0
result = filter(fun3,list2)
print(list(result))


#文件基本操作
#open(name,mode)    name:打开文件名的字符串（可谓具体路径）    mode：设置打开文件模式
#打开文件
f = open('D:\File\文档\练习文件夹\测试.txt','r',encoding='utf-8')
#文件写入    open中需写为‘w’
# f.write('hello world')
#读取文件中的信息，open中需换为‘r’
content = f.readlines()
print(content)
#关闭文件
f.close()


# #文件备份
# file_name = input('请输入要备份的文件:')
# #提取文件后缀点的下标
# index = file_name.rfind('.')
# print(index)     #打印下标值
# #打印源文件名无后缀
# print(file_name[:2])
# # 2.1 组织新文件名 旧文件名 + [备份] + 后缀
# new_name = file_name[:2]+'[备份]'+file_name[2: ]
# print(new_name)

#将备份文件写入数据
old_file = open('D:\File\文档\练习文件夹\测试.txt','rb')
new_file = open('D:\File\文档\练习文件夹\测试文件.txt','wb')
#将源文件数据写入备份文件中
while True:
    con = old_file.read(1024)
    if len(con) == 0:
        break
    new_file.write(con)
old_file.close()
new_file.close()

#文件夹创建，遍历，删除
#os模块
#需导入os模块
import os
#将目录切换至房前文件夹
os.chdir('D:\File\文档\练习文件夹')
#打印当前目录名称
print(os.getcwd())
#创建新的文件夹
# os.mkdir('D:\File\文档\练习文件夹\练习1')
#获取目录下所有文件
for i in os.listdir('D:\File\文档\练习文件夹'):
    print(i)
#删除文件夹
# os.rmdir('D:\File\文档\练习文件夹\练习1')


#批量修改文件名称，添加和删除指定字符串
import os
#设置标识
flag = 1
#获取指定目录
file_name = 'D:\File\文档\练习文件夹\新建文件夹'
print(file_name)
#获取指定目录
file_list = os.listdir(file_name)
print(file_list)
#遍历文件列表
for name in file_list:
    if flag == 1:
        new_name = 'python-' + name
    #删除指定字符
    elif flag == 2:
        num = len('python')
        new_name = name[num:]
    #打印新文件名，测试程序正确性
    print(new_name)
#     #重命名
#     os.rename(file_name + name,file_name + new_name)