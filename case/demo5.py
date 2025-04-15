
#编程第一步

#第一种情况
a = 0
b = 1
while b<10:
    print(b)
    a = b
    b = a+b                   #此时的a是赋值为后的a，即a=1

#第二种情况
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b             #此时的a未被赋值  a+b中的a=0


#条件控制语句                      if——elif——else
# age = int(input('请输入狗狗的年龄：'))
# if age < 0:
#     print('你在开玩笑吗？')
# elif age == 1:
#     print('相当于人类的14岁')
# elif age == 2:
#     print('相当于人类的22岁')
# elif age > 2:
#     age1 = 22 + (age - 2) *5
#     print('相当于人类年纪的：',age1,'岁')
# #退出提示
# print('点击enter退出')


#循环语句                     for和while
#                           while 判断条件(condition):       执行语句（statements）
#计算1到100的和
num = 1
sum = 0
while num <=100:
    sum = num +sum
    num+=1
print(sum)


#无限循环
# var = 1
# while var ==1:
#     num = input('请输入一个数字：',)
#     print(num)
# print('bye bye')

#while循环使用 else 语句
count = 0
while count < 5:               #条件语句为true时执行
    print(count,'小于5')
    count += 1
else:                          #条件语句为False执行
    print(count,'大于等于5')

#while语句只有一条语句，可以将该语句与while写在同一行
# var = 1
# while var ==1: print('相同')
# print('不相同')


#for 循环语句   使用break语句，跳出当前循环
#for循环作用于空迭代器上一次也不会执行，而是直接结束，不会报错
var1 = ['runoob','baidu','taobao','Goodle']
for a in var1:
    if a =='baidu':
        print('找到了！:',a)
        break
    print('循环数据',a)
else:
    print('没有循环数据')
print('循环完成！')

#range()函数       遍历数字序列   区间左闭右开
for i in range(5):
    print(i)
#range(5,9):数字5到9之间    指定区间
#range(0,10,3):数字0到10之间，以3个数字为间隔显示
#range(-10,-100,-30):可以为负数
#range(2,2):返回的是一个空的迭代器，

#break可跳出for和while的循环体
#continue跳出当前循环，继续下一循环

for i in 'runoob':
    if i == 'b':
        break
    print('当前字母为',i)
#break
var = 10
while var >0:
    print('当前变量为：',var)
    var = var-1
    if var ==5:
        break
print('结束了')
#continue
var = 10
while var >0:
    print('当前变量为：',var)
    var = var-1
    if var ==5:
        continue
print('结束了')


#for循环中嵌套for循环    break：直接跳出内层循环
for n in range(2, 10):
    for x in range(2, n):                   #内层循环中n在变换后，要从第一个值开始循环
        # print(x)
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')


#pass是空语句，一般用做占位符
for str in 'runoob':
    if str == 'o':
        pass
        print('执行pass块了')
    print('当前的str值为：',str)
print('结束了')





#迭代器                字符串，列表，元组，对象，都可用作迭代器
#有两个基本方法：iter() 和 next()
list = [1,2,3,4]
it = iter(list)
print(next(it))
print(next(it))

#迭代器可以使用常规的for循环进行遍历
list = [1,2,3,4]
it = iter(list)
for x in it:
    print(x,end=' ')

#创建一个迭代器        _iter_()  和   _next_()
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



#stoplteration 异常用于标识迭代的完成，可用于完成循环后触发stopltertion异常来结束迭代




#函数   以def关键字开头，后接函数标识名称和圆括号()
#语法定义：    def  函数名（参数列表）：     函数体
def max(a,b):
    if a > b:
        return a
    else:
        return b


#使用函数输出
def hello():
    print('hello world')
hello()           #调用函数

#使用函数比较
def max(a,b):
    if a > b:
        return a
    else:
        return b
a = 10
b = 20
print(max(a,b))


#计算函数面积
def area(width,hight):
    return  width * hight
def print_welcome(name):
    print('welcome',name)
print_welcome('runoob')
width = 20
hight = 30
print('宽width是：',width,'高hight是：',hight,'面积是：',area(width,hight))


#可更改对象与不可更改对象
#string,tuples,numbers 不可更改对象     list,dict  可修改对象
#不可边类型：变量a先赋值5，在赋值10，是a被新生成一个int值对象10，不是修改
#可变类型：变量la=[1,2,3] 在la[1]=10,则是将第二个元素修改


#通过id()函数查看内存地址变化
def change(a):
    print(id(a))
    a = 10
    print(id(a))
a = 1
print(id(a))
change(a)

#可变对象在函数内修改了参数
def change(mylisy):
    mylisy.append([1,2,3,4])
    print('函数内的值',mylist)
mylist = [11,22,33]
change(mylist)
print('函数外的取值',mylist)


#必需参数：须以正确的顺序传入函数，调用时的数量必须和声明时一样
def printme(str):
    print(str)
    return
printme(str)            #调用函数，括号内没有参数会进行报错

#关键字参数：函数调用关键字参数来确定传入的参数值
def printmee(str1):
    print(str1)
    return
str1 = '123'           #参数设置在外面
printmee(str1)

#参数需要与函数参数顺序相对应
def printmea(name,age):
    print('name的值是：',name)
    print('age的值是：',age)
    # return
name = 'zhangsan'
age = 12
printmea(name,age)          #顺序必须与函数顺序相对应


#调用时若参数没有传参，则取默认自带的参数
def printman(name,age = 20):
    print('name的值为：',name)
    print('age的值为：',age)
    return
printman(name='lisi',age=30)
print('-------------------')
printman(name='wangwu')                #调用时未传参，取默认的

#不定长参数  参数中printin（arg1,*arg2） 加入星号的参数会以元组的形式导入

def printmain(arg1,*arg2):
    print('arg1的值为：',arg1)
    print('arg2的值为：',arg2)
    return
# arg1 = 10
# arg2 = (11,22,33)
printmain(11,22,12,54,56,76,35)

#不指定函数
def printwan(arg1,*arg2):
    print('arg1的值为：',arg1)
    for var in arg2:
        print(var)
    return
printwan(11,22,33,44,55,66)

#不定长参数  参数中printin（arg1,**arg2） 加入两个星号的参数会以字典的形式导入
def printtwo(arg3,**arg4):
    print('arg3的值为：',arg3)
    print('arg4的值为：',arg4)
    return
printtwo(11,a =22,b = 33,c = 44,d = 5)

#如果单独出现星号 * 后的参数必须用关键字传入

#匿名函数      使用lambda来创建匿名函数
#lambda主体是一个表达式，不是代码块
#语法：         lambda arg1,arg2,arg3,arg4:expression
sum = lambda arg1,arg2:arg1+arg2
print('相加后的和为：',sum(11,22))

#return 语句
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total
# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)


