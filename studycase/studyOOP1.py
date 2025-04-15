#python面向对象基础

#定义一个类
#经典形
# class 类名：
#     代码

#新式型
# class 类名():
#     代码

#类的定义
class Person():
    def eat(self):
        print('我喜欢吃零食')
        print(self)
    def drink(self):
        print('我喜欢和果汁')


#类的实例化      对象名 = 类名（）
p1 = Person()
print(p1)
#用对象名调用实例方法
p1.eat()
p1.drink()

#添加和获取对象属性
#类外部添加对象属性       对象名.属性名称 = 值
p1.name = '张三'
p1.age = 13
p1.url = 'www.baidu.com'
#类外部获取对象属性       对象名.属性名
print(f'{p1.name}')
print(f'{p1.age}')

#在类里面获取对象名称
class People():
    def eat_test(self):
        print(f'{self.name}')
        print(f'{self.age}')
        print(f'{self.sex}')
p2 = People()
p2.name = 'luck'
p2.age = 18
p2.sex = '男'
p2.eat_test()

#魔法方法   _xxx_()  的函数叫做魔法方法   具有特殊功能的函数      _init_() 方法
class ManyPeople():
    #定义初始化功能的函数
    def __init__(self):
        # 添加实例属性
        self.name = '张三'
        self.age = 18
        self.addres = '杭州'
    def print_info(self):
        print(f'姓名为：{self.name},年纪为：{self.age},现居地为：{self.addres}')
pname = ManyPeople()
pname.print_info()


#带参数的__init__()
class ManyPeople():
    #定义初始化功能的函数  __init__(self) 方法传参
    def __init__(self,name,age,address):
        # 添加实例属性
        self.name = name
        self.age = age
        self.addres = address
    def print_info(self):
        print(f'姓名为：{self.name},年纪为：{self.age},现居地为：{self.addres}')
pname = ManyPeople('zhangsan','30','hangzhou')
pname.print_info()


#_str_()方法
class Person():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def __str__(self):
        #返回一个对象的描述信息
        return f'姓名为：{self.name}, 年纪为：{self.age}, 现居地为：{self.address}'
testp1 = Person('lisi','20','zhengzhou')
print(testp1)

#
# #__del__()方法
# class Person1():
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#     def __del__(self):
#         print(f'{self}对象已被删除')
# p2test = Person1()
# # print(p2test)


#案例1
class TestCase1():
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        if self.score >= 90:
            print(f'{self.name}的考试成绩为：{self.score},成绩为优秀')
        elif self.score >= 80:
            print(f'{self.name}的考试成绩为：{self.score},成绩为良好')
        elif self.score >= 70:
            print(f'{self.name}的考试成绩为：{self.score},成绩为中等')
        elif self.score >= 0:
            print(f'{self.name}的考试成绩为：{self.score},成绩为及格')
        else:
            print(f'{self.name}的考试成绩为：{self.score},成绩为不及格')
testcase1 = TestCase1('小明',88)
testcase1.print_score()


#案例2
class TestCase2():
    def __init__(self,name,wight):
        self.name = name
        self.wight = wight
    def run(self):
        print(f'{self.name},今天跑步了，减掉0.5斤')
        self.wight -= 0.5
    def eat(self):
        print(f'{self.name}今天吃肉了，长1斤')
        self.wight += 1
    def __str__(self):
        return f'姓名为：{self.name},体重为：{self.wight}'
testcase2 = TestCase2('小红',75)
# testcase2.run()
testcase2.eat()
print(testcase2)
