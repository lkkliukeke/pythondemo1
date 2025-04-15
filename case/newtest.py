#类的实例化
#python类的实例化
class TestDemo:
    #定义两个类变量
    name = '蜜雪冰城'
    add = '2'
    def __init__(self,name,add):
        #定义两个实例变量
        self.name = name
        self.add = add

        print(name,'的价格为：',add)                #123 的网址为： aaaaaa
    def say(self,content):
        print(content)
tests = TestDemo('123','aaaaaa')





#类的实例化
#python类的实例化
class TestDemo:
    #定义两个类变量
    hotelBoss="刘珂珂"
    hotelName = '蜜雪冰城'
    def __init__(self,drinkName,drinkPrice):
        #定义两个实例变量
        self.drinkName= drinkName
        self.drinkPrice= drinkPrice
        # print(drinkName,'价格为：',drinkPrice)                #123 的网址为： aaaaaa
    def says(self,drinkName,drinkPrice):
        print(drinkName,'价格为：',drinkPrice)
tests = TestDemo(drinkPrice = '柠檬水',drinkName = '13')
tests.says('水','34')

#若不先调用says方法，直接调用方法中的类则会报错
# tet = TestDemo()
# print(tests.drinkPrice)