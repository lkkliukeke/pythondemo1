#面向对象
class tortoise:
    bodycolor = '绿色'
    footnum = 4
    weight = 10
    hasshell = True

    #会爬
    def crawl(self):
        print('乌龟会爬')
    #会吃东西
    def eat(self):
        print('吃东西')
    #会睡觉
    def sleep(self):
        print('在睡觉')
    #会缩到壳里
    def protect(self):
        print('缩进了壳里')

#class类定义
class TheFirstDenmo:
    add = 'http://www.baidu.com'
    def case(self,str):
        print(str)
#创建一个空类
class empty:
    pass

#构造函数（构造方法）   _init_()    代码块：def _init_(self,...):  代码块
class TheFirstCase:
    #构造方法
    def __init__(self):
        print('调用构造方法')
    #定义一个类属性
    add = 'http://www.taobao .com'
    #定义一个say方法
    def say(self,content):
        print(content)
zhangsan = TheFirstCase()             #   调用构造方法

#在_init_()方法中自定义一些参数
class TestDemo:
    def __init__(self,name,add):
        print(name,'的网址为：',add)
test = TestDemo('张三','http://www.zhangsan.com')  #张三 的网址为： http://www.zhangsan.com





#类的实例化
#python类的实例化
class TestDemo:
    #定义两个类变量
    name = '张三'
    add = 'http://www.zhangsan.com'
    def __init__(self,name,add):
        #定义两个实例变量
        self.name = name
        self.add = add
        print(name,'的网址为：',add)                #123 的网址为： aaaaaa
    def say(self,content):
        print(content)
tests = TestDemo('123','aaaaaa')


#输出name和add的实例变量的值
print(tests.name,tests.add)                        #123 的网址为： aaaaaa

#修改实例变量的值
tests.name = '修改后的'
tests.add = 'http://www.xiugaihou.com'
print(tests.name,tests.add)                        #修改后的 http://www.xiugaihou.com

#调用say（）方法
tests.say('调用say方法')                            #调用后打印    调用say方法

#动态增加实例变量
tests.age = 'nan'
print(tests.age)                                  #    nan

#动态删除实例变量    删除后打印会报错
# del tests.age
# print(tests.age)





#self 用法详解
class a:
    def __init__(self,name):
        self.name = name
c = a('zhangsan111111')                        #    zhangsan111111
print(c.name)
# d = a('lisi123456')
# print(d.name)


#给类对象动态添加方法
def info(self):
    print('--info--函数',self)        #--info--函数 <__main__.a object at 0x0000022F9964D6D0>
c.foo = info
c.foo(c)
c.bar = lambda self: print('--lambda--表达式',self)    #--lambda--表达式 <__main__.a object at 0x0000022F9964D6D0>
c.bar(c)


def info1(self,content1):
    print('地址为：',content1)           #    地址为： 666666666
#导入MethodType
from types import MethodType
c.info1 = MethodType(info1,c)
#第一个参数已经绑定，无需传入
c.info1('666666666')



