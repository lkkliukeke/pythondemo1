
#使用断言       assert
# num = int(input('输入一个数字：'))
# #设置断言，在设置的范围内才会执行
# assert 0 <= num <= 60
# print('当前分数为：',num)

#zip函数 列中对应位置的元素重新组合，生成一个个新的元组。    zip(iterable)  iterable表示多个列表，元组，字典，range()区间
lists = [11,12,13]
lista = (33,55,77)
print([x for x in zip(lists,lista)])   #[(11, 33), (12, 55), (13, 77)]

list_dic = {33:1,32:2,31:3}
list_set = {55,66,87}
print([x for x in zip(list_dic)])       #[(33,), (32,), (31,)]

my_pychar = 'python'                #以最短的序列为准进行压缩
my_shechar = 'shell'
print([x for x in zip(my_pychar,my_shechar)])   # [('p', 's'), ('y', 'h'), ('t', 'e'), ('h', 'l'), ('o', 'l')]

#返回一个逆序排列的迭代器（遍历改逆序序列），不会修改原来序列中的元素顺序    reserved(seq) seq可以是列表，元素，字符串以及range()生成的区间
print([x for x in reversed([1,2,3,4,5,6])])      #列表进行逆序
print([x for x in reversed((1,2,3,4,5,6,7))])    #元组进行逆序
print([x for x in reversed('asdfghjkl')])        #字符串进行逆序
print([x for x in reversed(range(10))])          #range()生成区间进行逆序

#对序列进行排序,不会在原来的基础上进行修改       sorted(指定序列，自定义排序规则，升序/降序) ，函数会返回一个排好序的列表
a = [1,2,3,4,5]            #列表进行排序
print('列表进行排序',sorted(a,reverse=True))

b = (5,4,3,2,1)           #元组进行排序
print('元组进行排序',sorted(b))

c = {4:1,3:2,2:3,1:4}     #字典按照key进行排序
print('字典进行排序',sorted(c.items()))

d = 'abcdefg'
print('字符串进行排序',sorted(d,reverse=True))

chars=['http://c.biancheng.net',\
       'http://c.biancheng.net/python/',\
       'http://c.biancheng.net/shell/',\
       'http://c.biancheng.net/java/',\
       'http://c.biancheng.net/golang/']
print(sorted(chars))              #默认排序
print(sorted(chars,key=lambda x:len(x)))


#实现len()的封装

def len_test(str):
       lenth = 0
       for i in str:
              lenth = lenth+1
       return lenth
lenth = len_test('http://www.biancheng.net/python/')
print(lenth)

lenth = len_test("http://c.biancheng.net/shell/")
print(lenth)

#函数返回表达式
def test_dis(str1,str2):
       return str1 if str1 > str2 else str2
print(test_dis('32','23'))

#参数传递，实参和形参
def demo1(a):           #a为形参
       print(a)
b = '你猜一下'
demo1(b)                #b为实参

def demo2(obj):
       obj +=obj
       print('形参的值为：',obj)
print('----值传递----')
a = '测试一下'
print('a的值为：',a)
demo2(a)
print('实参的值为：',a)

#使用关键字参数形式
def demo3(str1,str2):
       print('第一个形参：',str1)
       print('第二个形参：',str2)
demo3('this is first','this is second')
demo3('this is first',str2='this is second')
demo3(str2='this is first',str1='this is second')

#自定义带有默认形参      自定义的必须位于所有没默认值参数的后面
def demo4(str1,str2='amazing'):
       print('第一个为：',str1)
       print('第二个为：',str2)
demo4('unbelievable')
demo4('believe','nothing')         #优先级高于形参定义
print(demo4.__defaults__)          #查看函数的默认值参数的当前值

#python的局部变量           函数的参数也属于局部变量
def demo5():
       case = 'this is case'
       print('内部变量为：',case)
demo5()
# print('外部变量为：',case)      #内部变量无法使用于外部

#python的全局变量
#在函数体外定义变量，一定为全局变量
add = 'runoob is good'
def test1():
       print('函数体内访问：',add)
test1()
print('函数体外访问：',add)

#在函数体外定义变量，使用global关键字对变量进行修饰后，就会成为全局变量
def test2():
       global add1
       add1 = 'this is new case'
       print('函数体内访问：',add1)
test2()
print('函数体外访问：',add1)

#获取指定作用域范围中的变量
#globals()函数        返回一个包含全局范围内所有变量的字典，键为变量名，值为该变量的值
pyname = '学习python'
pyadd = '了解python'
def text1():
       #局部变量
       case1 = 'runoob new'
       caseadd = 'taobao.com'
print(globals())
print(globals()['pyname'])
globals()['pyname'] = 'python入门教程'
print(pyname)

print('-----------------')
#locals()函数
pyname1 = '学习python'
pyadd1 = '了解python'
def text2():
       case2 = 'new runoob'
       caseadd2 = 'baidu.com'
       print('函数内部的locals：')
       print(locals())
text2()
print('函数外部的locals')
print(locals())

print('-----------------')
#vars(object)函数为内置函数，返回一个指定的object对象范围内所有变量组成的字典
pyname3 = '学习python'
pyadd3 = '了解python'
class demo:
       case3 = 'new runoob'
       caseadd3 = 'baidu.com'
print('有object')
print(vars(demo))
print('没有object')
print(vars())

#局部函数及用法
def outdef():       #全局函数
       def indef():       #局部函数
              print('调用局部函数')
       indef()            #调用局部函数
outdef()            #调用全局函数

#上面案例转换
def outdef():
       def indef():
              print('调用局部函数1')
       return indef
new_indef = outdef()
new_indef()

#使用nonlocal关键字
def outdef1():
       name = '所在函数中定义name变量'
       def indef1():
              nonlocal name
              print(name)
              name = '局部函数内定义变量'
       indef1()
outdef1()

#闭包函数（闭合函数）   计算一个数的n次幂
def new_power(str):
       def order_power(case):
              return case ** str
       return order_power      #返回值是order_power函数
# squer = new_power(2)    #计算一个数的平方
cube = new_power(3)     #计算一个数的立方
# print(squer(2))        #计算2的平方
print(cube(4))        #计算4的立方

#闭包属性 _closure_
# def nth_power(exponent):
#        def exponent_of(base):
#               return base ** exponent
#        return exponent_of
# square = nth_power(2)
# print(squer.__closure__)

#lambda表达式    匿名函数       name = lambda[list]:表达式
def name(x,y):
       return x + y
print(name(3,8))
#使用lambda
add = lambda x,y:x+y
print(add(3,6))

#执行字符串形式的代码
# eval(source,globals=None,locals=None)      添加_builtins_系统内置的key
# exec(source,globals=None,locals=None)    可以执行更加复杂的代码
dic = {}
dic['b'] = 3
print(dic.keys())
exec('a = 4',dic)
print(dic.keys())

a = 10
b = 20
c = 30
g = {'a':6,'b':8}
t = {'b':100,'c':10}
print(eval('a+b+c',g,t))

a = 1
exec ("a = 2")         #相当于执行 a=2
print(a)
a = exec("2+3")         #相当于执行 2+3,但是没有返回值，a应为None
print(a)
a = eval('2+3')         #相当于执行 2+3，并把结果返回给a
print(a)