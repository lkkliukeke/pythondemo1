
#列表练习题

#3.1 反转（判断对称）   判断一个数组是对称数组
def test1():
    list1 = [1,2,3,4,6,8]
    list2 = [8,6,4,3,2,1]
    list3 = []
    for i in list2:
        list3.insert(0,i)
    # print(list3)
    if list1 == list3:
        return True
    else:
        return False
print(test1())


#3.2 列表切片
a=[1,3,5,7,11]
a.reverse()            #反转列表
print('反转后列表：',a)
x = []
for i in a:            #取到奇数位值的数字
    b = a.index(i)
    if b%2 == 0:
        x.append(i)
print('奇数位数字：',x)


#3.3 列表大小排序
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
a.sort()                  #升序    sort(reverse = True)为降序
print('从小到大排序：',a)


#3.4 取出最大值最小值
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
print('列表最大值：',max(L1))
print('列表最小值：',min(L1))


#3.5 找出列表中单词最长的一个
def test4():
    a = ["hello", "world", "yoyo", "congratulations"]
    s = len(a[0])              # 把第一个元素的长度写出来
    m = ''
    for i in a:
        if len(i) > s:         #用第一个元素长度 比较 列表中的每个元素长度
            m = i              #把长度最大的赋值给 m
    return m
print(test4())


#3.6 切片取出列表中最大的三个数
l2 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
l2.sort()
print('排序后的l2:',l2)
x = l2[-3:]
print('截取的区间值为：',x)

# 3.7 列表按绝对值排序
a = [1, -6, 2, -5, 9, 4, 20, -3]
lists = []
for i in a:
    lists.append(abs(i))               #abs()    取绝对值
lists.sort()
print('绝对值排序后的列表：',lists)


#3.8 按字符串长度排序
b = ['hello', 'helloworld', 'he', 'hao', 'good']
#key=len 相当于：[len('hello'),len('helloworld'),len('he'),len('hao'),len('good')]
b.sort(key=len,reverse=True)            #sort进行排序  reverse=True逆序
print('排序后的列表：',b)


# 3.9 去重与排序
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
L1.sort()
L2 = []
for i in L1:
    if i not in L2:
        L2.append(i)
print('去重后的排序：',L2)


#3.11 列表合并
a = [1, 3, 5, 7]
b = ['a', 'b', 'c', 'd']
a = a + b
print('列表合并：',a)


#3.12 生成列表(列表推导式)
#用一行代码生成一个包含 1-10 之间所有偶数的列表  range(1,11,2)  步长为2
print([i for i in range(2,11)])     #列出2-10 之间的整数列表
print([i for i in range(2,11,2) if i%2==0])
a = range(2,11)


#3.13 列表成员的平方
x = [1,2,3,4,5]
b = []
for i in x:
    b.append(i**2)
print('列表的平方：',b)


#3.14 找出列表大于0的数
c = [1, 3, -3, 4, -2, 8, -7, 6]
lists = []
for i in c:
    if i > 0:
        lists.append(i)
print('列表大于0的数：',lists)


#3.15 统计在一个队列中的数字，有多少个正数，多少个负数
c = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
positive = []
minus = []
for i in c:
    if i > 0:
        positive.append(i)
    elif i < 0:
        minus.append(i)
    else:
        continue
a = len(positive)
b = len(minus)
print('正数的个数为：',a)
print('负数的个数为：',b)


# 3.16列表排除筛选  删除姓张的     第一种
a = ['张三','张四','张五','王二']
for i in a[:]:          #a[:]  其实就是复制a中的内容，并创建新的内存地址来存储
    # print(a[:])
    if i[0] == '张':
        a.remove(i)
print('删除后的列表1：',a)

# 3.16列表排除筛选  删除姓张的     第二种
a = ['张三','张四','张五','王二']
b = []
for i in a:
    if i[0] != '张':
        b.append(i)
print('删除后的列表2：',b)



#3.17列表过滤(filter)
n = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
def test_filter(n):
    return n > 0
newlist = filter(test_filter, n)
print('过滤后的列表：',list(newlist))


#3.18过滤列表中不及格学生(filter)
a = [
       {'name': '张三', 'score': 66},
       {'name': '李四', 'score': 88},
       {'name': '王五', 'score': 90},
       {'name': '陈六', 'score': 56},
    ]         # lambda 相当于是声明一个函数
print(list(filter(lambda x: x.get('score') > 60,a)))


#3.19找出列表中最大数出现的位置
a = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]
# print(max(a))
b = a.index(max(a))
print('最大数的位置：',b)


#3.20找出列表中出现次数最多的元素
def test_num():
    a = [
        'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
        'need', 'skills', 'more', 'my', 'ability', 'are',
        'so', 'poor'
    ]
    lists = {}
    for i in a:
        if i not in lists.keys():
            lists[i] = a.count(i)     #添加元素和数量到字典中以key：value的形式
    # return lists
    # return max(lists.values())
    # b = lists.items()
    # c = list(lists.keys())[list[lists.values().index('')]
    # return lists.items()
    return sorted(lists.items(), key=lambda x: x[1], reverse=True)[0][0]
print('出现最多的元素：',test_num())



#3.21 分别统计列表中每个成员出现的次数
def test_some():
    a = [
        'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
        'need', 'skills', 'more', 'my', 'ability', 'are',
        'so', 'poor'
    ]
    teste = {}
    for i in a:
        if i not in teste.keys():
            teste[i] = a.count(i)
    return teste
print('列表各个元素出现的次数：',test_some())


#3.22 列表查找元素位置
A1=[1, 'aa','val', 2, 'bb', 'val', 33]
def test_place(var,string):
    if string not in var:
        return -1
    else:
        return A1.index(string)
print(test_place(A1,'val'))


#3.23 列表查找两数之和
def test(target=9):
    num = [2, 7, 11, 15]
    # 统计数组的长度
    length = len(num)
    dicts = {}
    for i in range(length):
        # 添加两个 for 循环，第二次for循环时，循环的位置会比第一次循环多一次
        for j in range(i + 1, length):
            # 将循环后的数据放在列表中，利用字典 key 唯一的属性处理数据
            dicts.update({num[i] + num[j]: {i, j}})
    # 打印出来的数据，是元素的格式，按照题目，将数据转行成字典
    lists = []
    for nums in dicts[target]:
        lists.append(nums)
    return lists
print(test())



#3.24二维数组取值(矩阵)    取出2
a = [['A', 1], ['B', 2]]
print(a[1][1])


#3.25 二维数组拼接
a = [[1,2],[3,4],[5,6]]
testlist = []
for i in a:
    for j in i:
        testlist.append(j)
print(testlist)


#3.26 列表转字符串
L = [1, 2, 3, 5, 6]
k = map(str,L)        #map 把列表中的int类型转换成str类型
print(" ".join(k))


#3.27 两个列表如何得到字典
# a = ['a', 'b', 'c']
# b = [1, 2, 3]
# s = {}
# for i in a:
#     s.update(keyword(i))
