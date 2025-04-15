#python 封装
class Tests:
    def setname(self, name):
        if len(name) < 3:
            raise ValueError("名称长度必须大于3！")
        self.__name = name
    def getname(self):
        return self.__name
    #为name配置setter和getter方法
    name = property(getname, setname)
    def setadd(self,add):
        if add.startswith("http://"):
            self.__add = add
        else:
            raise ValueError("地址必须以http:// 开头")
    def getadd(self):
        return self.__add
    #为add配置setter和getter方法
    add = property(getadd, setadd)
    #定义一个私有方法
    def __display(self):
        print(self.__name,self.__add)
tests = Tests()
tests.name = 'c语言中文网'
# tests.name = '中文'           #长度不对会导致抛出异常
tests.add = 'http://c.biancheng.net'
# tests.add = 'https://c.biancheng.net'     #地址对不上就会导致报错抛出异常
print(tests.name)
print(tests.add)
# print(tests.__display)



#继承  让From继承Shape类
class Shape:
    def draw(self):
        print('画')
class From(Shape):        #From（子类）继承Shape（父类）
    def areas(self):
        are = 3 * 4
        print('结果为：',are)
froms = From()
froms.areas()
froms.draw()  #子类调用父类方法

#子类调用多个父类
class People:
    def say(self):
        print('我是一个人，我得名字是',self.name)
class Anmina:
    def display(self):
        print('我是另一个新方法')
#同时继承 People 和 Animal 类
#其同时拥有 name 属性、say() 和 display() 方法
class Person(People,Anmina):
    pass           #占位语句，如果定义一个空函数程序会报错，当你没有想好函数的内容是可以用 pass
person = Person()
person.name = 'zhangsan'
person.say()
person.display()


#python的多继承
#根据子类继承多个父类时这些父类的前后次序决定，即排在前面父类中的类方法会覆盖排在后面父类中的同名类方法。
class People:
    def __init__(self):
        self.name = People
    def say(self):
        print('People类',self.name)
class Animal:
    def __init__(self):
        self.name = Animal
    def say(self):
        print('Animal类',self.name)
class Person(People,Animal):
    pass
person = Person()
person.name = '张三'
person.say()


#python父类方法重写
class Bird:
    def isWinge(self):
        print('鸟有翅膀')
    def fly(self):
        print('鸟会飞')
class Ostrich(Bird):
    def fly(self):      #重写父类方法
        print('鸵鸟不会飞')
ostrich = Ostrich()
ostrich.fly()
ostrich.isWinge()
#调用被重写的方法
Bird.fly(ostrich)



#调用父类的构造方法
class People:
    def __init__(self,name):
        self.name = name
    def say(self):
        print('我是人，我的名字是',self.name)
class Animal:
    def __init__(self, food):
        self.food = food
    def display(self):
        print('我是动物，我吃',self.food)
class Person(People,Animal):
    pass
per = Person('zhangsan')
per.say()


#在子类中的构造方法中，调用父类构造方法的方式有 2 种，分别是：
#类可以看做一个独立空间，在类的外部调用其中的实例方法，可以向调用普通函数那样，只不过需要额外备注类名（此方式又称为未绑定方法）；
#使用 super() 函数。但如果涉及多继承，该函数只能调用第一个直接父类的构造方法
#使用super()方法
class People:
    def __init__(self,name):
        self.name = name
    def say(self):
        print('我是人，我的名字是',self.name)
class Animal:
    def __init__(self, food):
        self.food = food
    def display(self):
        print('我是动物，我吃',self.food)
class Person(People,Animal):
    #自定义构造方法
    def __init__(self, name,food):
        #调用People类的构造方法
        super().__init__(name)
        #调用其他父类的构造方法，需手动给self传值     ,使用未绑定方法
        Animal.__init__(self,food)
per = Person('zhangsan','熟食')
per.say()
per.display()