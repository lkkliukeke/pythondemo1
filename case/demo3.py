
#列表   使用方括号[]   列表数据可进行修改或更新     列表未字符串是比较的是ASCII  即为字符的ID


#函数
#列表元素个数           len(list)
#返回列表元素最大值      max(list)
#返回列表元素最小值      min(list)
#元组或字符串转换为列表          list(seq)   seq:为要转换的元组或字符串
atuple = (1,2,3,4,5)              #元组转换
lists = list(atuple)
print(lists)

atuples = 'thank you'             #字符串转换
list1 = list(atuples)
print(list1)

# 索引号从左到右0开始    ，从右到左-1开始    区间范围：左闭右开
list = ['red','blue','pink','green','black','white','yellow']
print(list)
print(list[2])               #获取单个元素，索引从左
print(list[0])               #获取单个元素，索引从左
print(list[-1])              #获取单个元素，索引从右
print(list[2:5])             #获取区间元素
list[4] = 'gry'              #修改原列表中下标为4 的元素为gry
print(list)
del list[5]                  #删除列表中第五个元素
print(list)

#组合两个列表
str1 = [1,2,3]
str2 = [4,5,6]
print(str1 + str2)

#重复列表  在一个列表中重复元素
str = ['1',1]*3
print(str)

#迭代                              end = ' '可以用于将结果输出到同一行
for x in [1, 2, 3]:
    print(x, end=" ")      #end=" " 输出结果在一行显示，不进行换行
print('\n')

#嵌套列表
a = [1,2,3]
b = [4,5,6,7]
c = [a,b]
print(c)
print('下标为1的元素',c[1])               #输出c列表下标为1的元素
print(c[1][2])            #查找列表中嵌套列表内的元素






#列表相关方法

#在列表末尾添加新的对象                      list.append(obj)   obj:添加到末尾的对象
list1 = ['Goodle','Runoob','Taobao','Jingdong']
print(list1)
list1.append('Baidu')
print(list1)


# #用于在列表末尾一次性追加另一个序列中的多个值     list.extend(seq)   seq:可以为元素，元组，字典
# list2 = ['Goodle','baidu','runoob']
# list3 = list(range(5))   #创建1-4的列表
# list2.extend(list3)      #方法不能写在打印中
# print(list2)              #['Goodle','baidu','runoob','1','2','3','4','5']
# tuple = ('123','456')
# list2.extend(tuple)      #添加元组到列表中
# print(list2)               #['Goodle','baidu','runoob','1','2','3','4','5','123','456']


#用于统计某个元素在列表中出现的次数             list.count(obj)   obj:列表中统计的对象
list2 = ['baidu','goodle','taobao','baidu','baidu','taobao']
print(list2.count('baidu'))

#用于从列表中找出某个值第一个匹配项的索引位置,找不到抛异常      list.index(x,beg,end)  x:所查找对象
list3 = ['Goodle','baidu','taobao','runoob']
print(list3.index('taobao'))
print(list3.index('baidu',1))      #从列表下标为1开始查找

#用于将指定对象插入到列表指定的位置           list.insert(index,obj) index:插入的索引位置 obj:插入列表的对象
list4 = ['Goodle','baidu','runoob','taobao']
list4.insert(1,'123')       #方法不能写在打印中
print('对象插入结果：',list4)

#用于移除列表中的一个元素(默认为列表最后一个元素)，并返回该元素的值      list.pop(index=)  index:要移除列表元素的索引值
list5 = ['Goodle','taobao','baidu']
print(list5.pop())             #打印移除的元素值,默认为列表最后一个元素
print('移除列表：',list5)                   #打印移除后的列表
print(list5.pop(0))            #根据索引值移除元素
print(list5)

#用于移除列表中某个值的第一个匹配项                     list.remove(obj)  obj:列表中要移除的对象
list6 = ['Goodle','taobao','runoob','baidu','runoob']
list6.remove('runoob')        #写在打印外      删除第一个匹配的值
print(list6)

#用于反向列表中元素,对列表元素进行反向排序               list.reverse()
list7 = ['Goodle','taobao','runoob','baidu']
list7.reverse()                #写在打印外
print('反向列表排序',list7)

#用于对原列表进行排序                        list.sort(key=None,reverse=False)
                            #key:用来进行比较的元素  reverse:为True时降序，False升序（默认）
list8 = ['Goodle','taobao','runoob','Facebook','baidu']
list8.sort()           #默认为升序排列
print('升序排序结果',list8)
vocal = ['e','r','G','T','f']
vocal.sort(reverse=True)    #设置为降序排列
print('降序排序结果',vocal)

#指定以括号中第二个元素排列
def takeSecond(elem):
    return elem[1]
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort()
print('原排序列表：',random)             #原排序，以括号中第一个元素排列
# 指定第二个元素排序
random.sort(key=takeSecond)
# 输出类别
print('排序列表：', random)

#用于清空列表                       list.clear()
list9 = ['Goodle','baidu','taobao','runoob']
print('未清除前：',list9)
list9.clear()
print('清除后：',list9)

#用于复制列表                        list.copy()
list10 = ['Goodle','baidu','taobao','runoob']
list11 = list10.copy()
print('复制后的列表：',list11)


print('\n')
print('\n')









#元组  使用小括号()     只有一个元素时，元素后需加上逗号，    元组中元素不允许修改
tup = (2,3,4,5)
print(type(tup))          #查看类型

tup1 = ('runoob')       #只有一个元素时，元素后需加上逗号,若不加，则视为运算符
print(type(tup1))            #type= str
tup2 = ('Goodle',)      #只有一个元素时，元素后需加上逗号,类型则为元组
print(type(tup2))            #type= tuple

#使用下标访问元组中的值
tup3 = ('Goodle','taobao','runoob','baidu')
print(tup3[2])
print(tup3[1:3])

#元组进行连接组合   组合到一个元组中
tupp1 = ('a','vv','hh',3)
tupp2 = ('ee',7,8,9)
tupp3 = tupp1+tupp2
print('连接组合：',tupp3)

#删除元组    元组中的元素值不允许删除，可使用del删除整个元组
tup4 = ('Goodle','taobao','baidu')
print(tup4)
# del tup4              #删除整个元组
# print(tup4)

#重复列表  在一个元组中重复元素
str = ('1',3)*3
print(str)

#迭代
for x in (1, 2, 3):
    print(x, end=" ")
print('\n')

#元组截取
tup5 = ('red','blue','pink','green','black','white','yellow')
print(tup5[2])               #获取单个元素，索引从左
print(tup5[0])               #获取单个元素，索引从左
print(tup5[-1])              #获取单个元素，索引从右
print(tup5[2:5])             #获取区间元素


#元组内置函数   重新赋值的元组，是绑定到新对象了，而不是修改了原来的对象
#计算元组元素个数               len(tuple)
#返回元组中元素最大值            max(tuple)
#返回元组中元素最小值            min(tuple)
#将迭代系列转换为元组            tuple(iterable)
list = ['Goodle','taobao','baidu','runoob','222','679']
tuple6 = tuple(list)
print(tuple6)                     #将列表list转换为元组


print('\n')
print('\n')






#字典   使用花括号{}  以键值对形式存在  key:value
#      使用字典里的键访问数据   若输入不存在的键，则或报错
dict = {'name':'runoob','age':'10','class':'first'}
print(dict['name'])                      #把响应的键放到打印中，打印出值
print(dict['age'])

#修改字典   有对应的键时为修改 ，没有相应的键时为增加
dict1 = {'name':'runoob','age':'10','class':'first'}
dict1['age'] = 18                        #修改年龄为18
dict1['sex'] = '男'                      #添加性别为男
print('修改后的字典：',dict1)

#删除字典      删除键后，值就没了
dict2 = {'name':'runoob','age':'10','class':'first'}
del dict2['name']                        #删除键‘name’
print('删除name后的：',dict2)
dict2.clear()                            #清空字典
del dict2                                #删除字典

#字典键特性
#同一个键不允许出现两次，若创建两次，后面的值会被记住
dict3 = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print ("有重复的键dict3['Name']: ", dict3['Name'])

#键是必须不可变的，可以用数字，字符串或元组充当，但列表就不行
# dict4 = {['Name']: 'Runoob', 'Age': 7}
# print ("dict['Name']: ", dict['Name'])              #会报错


#内置函数
#计算字典元素个数，即键的总数              len(dict)
#输出字典，以字符串表示                   str(dict)
# dict5 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print(str(dict5))

#返回变量类型                            type(dict)
dict5 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(type(dict5))




#内置方法
#删除字典内所有元素                        clear()
dict1 = {'name':'runoob','age':'10'}
print(len(dict1))
print('清除字典：',dict.clear())

#返回字典的浅复制                          copy()
dict2 = {'name':'runoob','age':'16','class':'First'}
dict3 = dict2.copy()          # 浅拷贝：深拷贝父对象，子对象不拷贝
print('新复制的字典：',dict3)

#用于创建一个新字典                         fromkey(seq,value)   seq:字典键列表  value:设置键对应值
seq = ('name','age','sex')
dict4 = dict.fromkeys(seq)                #只设置新字典的键，值为none
print(dict4)
dict4 = dict.fromkeys(seq,10)             #设置新字典的键和值
print(dict4)

#返回指定键的值                           get(key,default)  key:字典中查找的键  default：若键不存在，返回默认值
dict5 = {'name':'runoob','age':'12','sex':'nan'}
print(dict5.get('name'))                         #字典中有name键
print(dict5.get('class','first'))                #字典中没有的字段，返回值
print('get方法',dict5)                          #未在字典中的键和值，不会添加到字典内

#字典中的in操作符用于判断键是否存在于字典中，在返回True，否返回False       not in刚好相反   key in dict
dict6 = {'name':'runoob','age':'12','sex':'nan'}
if 'name' in dict6:
    print('键在字典中')
else:
    print('键不在字典中')

if 'class' not in dict6:
    print('键不在字典中')
else:
    print('键在字典中')


#以列表返回视图对象，组合型的返回key和value                  items()
dict7 = {'name':'zhangsan','age':'16','sex':'nan'}
print(dict7.items())       #dict_items([('name', 'zhangsan'), ('age', '16'), ('sex', 'nan')])


#返回一个视图对象                               keys()    values()
dict8 ={'name':'lisi','age':'18','sex':'nan'}
keys = dict8.keys()
values = dict8.values()
print(keys)
print(values)

#关于字典中 get() 和 setdefault() 的区别：
#主要在于当查找的键值 key 不存在的时候，setdefault()函数会返回默认值并更新字典，添加键值；
# 而 get() 函数只返回默认值，并不改变原字典

#若键不存在于字典中，将添加键并将值设为默认            setdefault(key,default)  key:查找的键值  default：键不存在时，设置默认键
dict9 = {'name':'runoob','age':'17'}
print(dict9.setdefault('age'))
print(dict9.setdefault('sex',None))               #不存在字典中的添加，会更新在字典中
print(dict9)

#把当前字典的内容添加到另一个字典中                    dict.update(dict1)  dict1:添加到指定的字典
dict10 = {'name':'ruoob','age':'17'}
dict11 = {'sex':'nan'}
dict10.update(dict11)                         #把dict11中的值更新到dict10 中
print(dict10)

#随机返回并删除字典中的最后一对键和值                   popitem()
dict12 = {'name':'lisi','alexa':'10000','url':'www.runoob.com'}
popobj = dict12.popitem()
print(popobj)                                 #移除的键和值
print(dict12)                                 #移除后的字典






