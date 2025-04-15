#python面向对象高级
#面向对象的三大特性：封装、继承、多态

#python 的继承
#基础语法
#父类B
class B(object):
    pass
#子类A
class A(B):
    pass

#案例1
class Animal(object):
    def eat(self):
        print('吃食物')
    def sleep(self):
        print('睡觉')
    def call(self):
        print('会叫')
class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog = Dog()
dog.eat()


print('-------案例1----------')
#案例
class Animal(object):
    # def __init__(self,name,age):      #打开会影响下面的程序运行，此条为案例
    #     self.name = name
    #     self.age = age
    def eat(self):
        print('吃东西')
    def sleep(self):
        print('睡觉')
    def call(self):
        print('叫。。。')
class Dog(Animal):
    def call(self):
        print('汪汪叫')
class Cat(Animal):
    def call(self):       #此方法被子类重构
        print('喵喵叫')
#Dog实例对象
dog1 = Dog()
dog1.eat()
dog1.call()
#Cat实例对象
cat1 = Cat()
cat1.sleep()
cat1.call()


print('-------案例2----------')
#调用父类属性和方法    super()   完整写法：super(当前类名，self).属性或方法
class Animal(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('吃食物')
    def sleep(self):
        print('睡觉')
    def call(self):
        print('叫声。。。')
class Dog(Animal):
    def __init__(self,name,age,sex):
        super().__init__(name,age)
        self.sex = sex
    def __str__(self):
        return f'{self.name},今年{self.age}岁了，性别为{self.sex},会汪汪叫'
class Cat(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name,age)
        self.sex = sex
    def __str__(self):
        return f'{self.name},今年{self.age}岁了，会喵喵叫'
# Dog实例对象
snoopy = Dog('Snoopy', 2, '男')
print(snoopy)
# Cat实例对象
kitty = Cat('Kitty', 1, '女')
print(kitty)


#python中的多继承实现    一个类同时继承多个父类
class Father(object):
    pass
class Mother(object):
    pass
class Son(Father,Mother):
    pass




print('-------多态案例1----------')
#python中的多态    案例1
class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def call(self):
        print(self.name,'会叫')
class Cat(Animal):
    def __init__(self,name,age,sex):
        super(Cat, self).__init__(name,age)
        self.sex = sex
    def call(self):
        print(self.name,'它会‘喵喵’叫')
class Dog(Animal):
    def __init__(self,name,age,sex):
        super(Dog, self).__init__(name,age)
        self.sex = sex
    def call(self):
        print(self.name,'它会‘汪汪’叫')
def do(all):
    all.call()
a = Animal('小黑',12)
b = Cat('小白',16,'男')
c = Dog('小张',17,'女')
for x in (a,b,c):
    do(x)



print('-------多态案例2----------')
#python多态    案例2
class Dog(object):
    def work(self):
        print('会工作')
class DogSon1(Dog):
    def work(self):
        print('会喝水1')
class DogSon2(Dog):
    # print('nihao')    将下面的函数注释掉后，就会调用父类方法
    def work(self):
        print('会喝水2')
class Person(object):
    #写一个函数 通过子类来调用work
    def user_dog(self,use):
        use.work()
son1 = DogSon1()
son2 = DogSon2()

person = Person()
#通过传函数所赋的值
person.user_dog(son1)
person.user_dog(son2)


print('-------面向对象得私有属性和私有方法----------')
#面向对象得私有属性和私有方法
class Girl():
    def __init__(self):
        self.name = '小红'
        self.__age = 19
    def __showinfo(self):
        print('姓名：%s，年龄：%d'%(self.name,self.__age))
girl = Girl()
print(girl.name)
#以下为私有属性和方法，外界不能直接访问
# print(girl.__age)
# girl.__showinfo()



print('-------私有属性和方法不能被子类继承----------')
#私有属性和方法不能被子类继承
class bird():
    def __init__(self):
        self.name = '露露'
        self.skill = '闪现，眩晕，斩杀，干扰，惩戒'
        self.__privatekill = '大招会飞'
class Tiger(bird):
    pass
tiger = Tiger()
tiger.name = '配擒虎'
#以下注释代码中  __privatekill为私有属性运行则会报错
# print(f'{tiger.name}所带的技能为:{tiger.skill}，他的大招为{tiger.__privatekill}')
print(f'{tiger.name}所带的技能为:{tiger.skill}')



print('-------获取和设置私有属性值----------')
#获取和设置私有属性值  一般定义get_xx 获取私有属性   定义set_xx 修改私有属性
class Girls():
    def __init__(self):
        self.name = '小明'
        self.__age = 20
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
girls = Girls()
#修改私有属性
girls.set_age(99)
print(girls.get_age())



print('-------类属性和实例属性----------')
#类属性和实例属性
class Tool(object):
    #定义一个类属性用来计算创建了多少个工具对象
    count = 0
    def __init__(self,name):
        self.name = name
        #针对类属性做一个计算
        Tool.count +=1
tool1 = Tool('张飞')
tool2 = Tool('韩信')
tool3 = Tool('张飞')
print(Tool.count)



print('-------类方法 ----------')
#类方法    针对类对象定义的方法   在类方法中可以直接访问类属性或调用其他类方法
# 语法 ：
# @classmethod    使用前面修饰器来标识，解释器这是一个类方法类方法的第一个参数应该是" cls "
# def 类名(cls)：
#     pass

#案例
class Tools(object):
    count = 0

    @classmethod
    def show_tool_count(cls):
        print(f'总共工具的个数为：{cls.count}')

    def __init__(self, name):
        self.name = name
        #针对类属性做一个计算
        Tools.count += 1
tools1 = Tools('diaochan')
tools2 = Tools('xiaoqiao')
tools3 = Tools('zhenji')
tools3 = Tools('nihao')
#输出工具对象的总数
Tools.show_tool_count()


#静态方法    既 不需要访问实例属性或者调用实例方法  也 不需要访问类属性或者调用类方法  可封装为一个静态方法

# @staticmethod
# def 静态方法名（）
#     pass

print('------静态方法案例-----------')
class Game1:
    @staticmethod
    def meun():
        print('开始[1]')
        print('暂停[2]')
        print('退出[3]')
Game1.meun()



print('-------综合案例---------')
class Game:
    #历史最高分
    top_score = 0
    def __init__(self,player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print('游戏帮助信息...')

    @classmethod
    def show_top_score(cls):
        print(f'历史最高分:{cls.top_score}')

    def start_game(self):
        print(f'开始游戏啦,{self.player_name}')
#显示游戏帮助
Game.show_help()
#显示历史最高分
Game.show_top_score()
#开始游戏
game = Game('nihao')
game.start_game()



print('-----重写_new_方法-------')
class MusicPlar(object):
    def __new__(cls, *args, **kwargs):
        print('创建对象，分配空间')
        instance = super().__new__(cls)
        return instance
    def __init__(self):
        print('播放器初始化')
player = MusicPlar()
print(player)




print('------python种的单例---------')
class MusicPlarer(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

player1 = MusicPlarer()
print(player1)

player2 = MusicPlarer()
print(player2)