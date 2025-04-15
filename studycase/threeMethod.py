#三大方法：实例方法，静态方法，类方法
#实例方法的第一个参数为 self ，表示一个具体的实例本身
#使用了@staticmethod  表示的为静态方法
#使用了@classmethod   表示为类方法  第一个参数为 cls
class Foo(object):
    '类的三种方法语法形式'
    def instance_method(self):
        print('一下为实例方法{}'.format(Foo))

    #静态方法
    @staticmethod
    def static_method():
        print('现在是静态方法')

    #类方法
    @classmethod
    def class_method(cls):
        print('现在是类方法')
foo = Foo()
foo.instance_method()
foo.static_method()
foo.class_method()
print('----------静态方法和类方法可以直接使用类名调用-----------')
Foo.static_method()
Foo.class_method()
#说明：实例方法只能被实例对象调用，
# 静态方法(由@staticmethod装饰的方法)、类方法(由@classmethod装饰的方法)，可以被类或类的实例对象调用



print('------第二个案例-------')
#静态方法和类方法使用的区别    python中只有一个初始化方法，
class Book(object):
    def __init__(self,title):
        self.title = title

    @classmethod
    def class_method(cls,title):
        book = cls(title=title)
        return book

    @staticmethod
    def static_method(title):
        book = Book(title)
        return book
book1 = Book('使用实例方法')
book2 = Book.class_method('使用类方法')
book3 = Book.static_method('使用静态方法')
print(book1.title)
print(book2.title)
print(book3.title)




print('------第三个案例------')
#静态方法调用另一个静态方法，如果改用类调用静态方法可以让cls代替
class Foolish(object):
    x = 1
    y = 2

    @staticmethod
    def average(*num):
        return sum(num)/len(num)

    @staticmethod
    def static_method():
        print('在静态方法中调用静态方法')
        return Foolish.average(Foolish.x,Foolish.y)

    @classmethod
    def class_method(cls):
        print('在类方法中调用静态方法')
        return cls.average(cls.x,cls.y)
foolish = Foolish()
print(foolish.static_method())
print(foolish.class_method())



print('-------第四个案例-----------')
#继承类中的区别
class Foos(object):
    x = 1
    y = 2

    @staticmethod
    def averag(*nums):      #父类中的静态方法
        return sum(nums)/len(nums)

    @staticmethod
    def static_method():     #父类中的静态方法
        print('父类中的静态方法')
        return Foos.averag(Foos.x,Foos.y)

    @classmethod
    def class_method(cls):   #父类中的类方法
        print('父类中的类方法')
        return cls.averag(cls.x,cls.y)

class Sons(Foos):
    x = 3
    y = 5

    @staticmethod
    def averag(*nums):       #子类中重载了父类中的静态方法
        print('子类中重载了父类中的静态方法')
        print('666',nums)
        return sum(nums)/3

p = Sons()
print("result of p.averag(1,5)")
#子类继承父类的方法，子类覆盖了父类的静态方法
print (p.averag(1,5))
print("result of p.static_method()")
#子类的实例继承了父类的static_method静态方法，调用该方法，还是调用的父类的方法和类属性
print(p.static_method())
print("result of p.class_method()")
#子类的实例继承了父类的class_method类方法，调用该方法，调用的是子类的方法和子类的类属性
print(p.class_method())





