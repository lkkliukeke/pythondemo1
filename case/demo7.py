
#python的输入和输出
#   str()：函数返回一个用户易读的表达形式
#   repr()：产生一个解释器易读的表达形式
import sys

s = 'hello,runoob'
print(str(s))
print(repr(s))

x = 10 * 2.35
y = 200 * 200
s = 'x的值为：'+repr(x)+',y的值为：'+repr(y)+''
print(s)
#repr()函数可以转义字符串中的特殊字符
hello = 'hello runob\n'
print(hello)
hellos = repr(hello)
print(hellos)
#repr()的参数可以是python的任何对象  可以为变量，列表......
var = repr((x,y,('goodle','runoob')))
print(var)

#输出一个平方和立方的表
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3),repr(x*x*x).rjust(4))

#输出一个平方和的立方表
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
     # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))

#在数字左边填充0                     zfill(2)  填充数字与数字总数有关
str2 = '12'.zfill(1)
print(str2)

#str.format() 基本用法      可以将值直接填充
print('{}网址：“{}!”'.format('菜鸟教程','www.ruunoob.com'))

#括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
#在括号中的数字用于指向传入对象在 format() 中的位置
print('{0} 和 {1}'.format('Google','runoob'))
print('{1} 和 {0}'.format('Google','runoob'))

#位置及关键字参数可以任意结合
print('站点列表 {0},{1},{other}。'.format('baidu','jingdong',other='taobao'))

#使用导入圆周率
import math
print('常量的值为：{}'.format(math.pi))

#用于在 : 后传入一个整数
table = {'baidu':1,'Google':2,'taobao':3}
for name,value in table.items():
    print('{0:10} ==> {1:10d}'.format(name,value))

#读取键盘输入    输入框
# str = input('请输入：')
# print('您输入的内容是：',str)

#打开一个文件  open('', '')   第一个参数为要打开的文件名   第二个参数为，描述文件如何使用
#关闭打开的文件  close()


#文件对象的方法
#为了读取一个文件的内容                             f.read()
#从文件中读取单独的一行                             f.readline()
#将返回该文件中包含的所有行                          f.readlines()
#将string写入到文件中，然后返回写入的字符数            f.write()
#返回文件对象当前所处的位置，从文件开头算起的字节数       f.tell()
#改变文件当前的位置                                 f.seek()
#在文本文件中，相对于文件的起始位置进行定位              f.close()


#异常处理      try/except
#先执行try语句，若有异常执行except语句
# while True:
#     try:
#         x = int(input('请输入数字：'))
#         break
#     except ValueError:                     #ValueError    值错误
#         print('你输入的不是一个数字')

#try(执行代码)/except（发生异常时执行的代码）/else（没有异常时执行的代码）
for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
    except IOError:
        print('cannot open',arg)
    else:
        print(arg, 'has',len(f.readlines()),'lines')
        f.close()

#try-finally  语句无论是否发生异常都会的代码
#try（执行代码）/except（发生异常时执行的代码）/alse（没有异常时执行的代码）/finally（不管有没有异常都执行的代码）
try:
    print()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话无论有没有异常都会执行')


#抛出异常
#raise语句       raise Exception()
x = 10
if x > 5:
    raise Exception('x 不能大于5 x的值为：{}'.format(x))

