
#集合   使用大括号{} 或者set() 创建函数  创建空集合必须使用set()        {}是用来创建空字典的

#创建格式
parame = {'value1','value2'}
parame1 = set('value3')
print(parame)
print(parame1)

#实例
basket = {'apple','orange','apple','banana','orange','pear'}
print('实例结果去重：',basket)                       #去重功能

#判断是都在集合内
if 'apple' in basket:
    print('在集合中')
else:
    print('不在集合中')

#两个集合间的运算
a = set('asdvdfwisbs')
b = set('safgwieufbc')
print(a)
print(b)
print(a-b)                      #a中包含b中不包含
print(a|b)                      #a或b中包含所有元素
print(a & b)                    #a和b的交集
print(a ^ b)                    #a和b中不相同的



#添加元素                                         s.add(X)  将元素x添加到集合s中
thisset = set(('Goodle','baidu','taobao','runoob',))
print(thisset)
thisset.add('zhangsan')            #向列表中添加一个元素,在列表中随机出现
print('添加一个元素时：',thisset)

#添加元素   x可以是元素，列表，元组，字典等              s.update(x)
thisset1 = set(('Goodle','baidu','taobao','runoob',))
print(thisset1)
thisset1.update({1,3})               #添加一个集合
print('添加一个集合：',thisset1)
thisset1.update([1,2],[3,4])
print('添加一个列表：',thisset1)

#移除元素      若移除元素不存在，则会报错                                 s.remove(X)  将元素x从集合s中移除
thisset2 = set(('Goodle','baidu','taobao','runoob',))
thisset2.remove('baidu')
print('移除后的集合：',thisset2)

#移除元素      若移除元素不存在，不会发生报错            s.discard(x)  将元素x从集合s中移除
thisset3 = set(('Goodle','baidu','taobao','runoob',))
thisset2.discard('baidu')
print('移除后的集合：',thisset2)

#删除元素      随机删除集合中的元素                     s.pop()
thisset3 = set(('Goodle','baidu','taobao','runoob',))
thisset3.pop()
print('随机删除后的集合：',thisset3)

#计算集合元素个数                                     len(s)    计算集合s元素个数
thisset4 = set(('Goodle','baidu','taobao','runoob',))
print('集合元素个数：',len(thisset4))

#清空集合                                            s.clear()
thisset5 = set(('Goodle','baidu','taobao','runoob',))
print('清空后的集合：',thisset5.clear())

#判断元素是否在集合中存在                               x in s  x:元素   s:集合
thisset5 = set(('Goodle','baidu','taobao','runoob',))
if 'taobao' in thisset5:
    print('元素在集合中')
else:
    print('不在集合中')






#集合内置方法

#添加元素                                         s.add(X)  将元素x添加到集合s中
#清空集合                                         s.clear()
#删除元素      随机删除集合中的元素                     s.pop()
#移除元素      若移除元素不存在，则会报错                s.remove(X)  将元素x从集合s中移除到
#添加元素   x可以是元素，列表，元组，字典等              s.update(x)
#拷贝一个集合                                      copy()
test1 = {'apple','orange','banana'}
test2 = test1.copy()
print('复制的集合：',test2)

#返回多个集合的差集，返回一个新集合                    difference(set)  set:必需，用于计算差集的集合
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)                                  #返回元素包含在集合X，但不包含在集合y
print('两个集合的差集：',z)

#用于移除两个集合都存在的元素                         difference_update(set) set:必需，用于计算差集的集合
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)                                  #移除两个集合都包含的元素
print('移除两个集合都存在的元素：',x)


#移除指定的集合元素                                  set.discard(value) value:必需，要移除的元素
test3 = {'apple','orange','banana'}
test3.discard('apple')
print('移除后的集合：',test3)

#返回两个或多个集合中都包含的元素，即交集              intersection(set1,set2....) set1:必需，查找相同元素的集合
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print('两个集合的交集：',z)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
test = x.intersection(y,z)
print('三个集合的交集',test)

#返回两个或多个集合中都包含的元素，即计算交集          intersection_update(set1,set2....) set1:必需，查找相同元素的集合
#intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，
# 而 intersection_update() 方法是在原始的集合上移除不重叠的元素
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print('两个集合的交集：',x)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print('三个集合的交集：',x)

#判断两个集合中是否包含相同元素，不包含返回True，包含返回False              isdisjoint(set) set:必需，要比较的集合
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print('两个集合中是否有相同的元素：',z)                                 #False


#用于判断集合的所有元素是否都包含在指定集合中，是返回True 否返回False        issubset(set) set:必需，要比查找的集合
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)                                                          #True


#用于判断指定集合的所有元素是否都包含在原始的集合中，是返回 True，否返回 False    issuperset(set) set:必需，要比查找的集合
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)                                                          #True

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)                                                          #False

#返回两个集合中不重复的元素集合，会移除两个集合中都存在的元素            symmetric_difference(set)  set -- 集合
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.symmetric_difference(y)
print('两个集合不重复的元素：',z)


#移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
#                                  symmetric_difference_update(set)   set:要检测的集合
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
x.symmetric_difference_update(y)
print('移除后的集合：',x)


#返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次     union(set1, set2...) set1:必需，合并的目标集合
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}
z = x.union(y)
print('两个集合除去相同元素：',z)

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print('三个集合除去相同元素：',result)