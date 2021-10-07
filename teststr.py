
#公众号字符串练习题


#1.2 判断字符串是否是回文     3223 反过来也是3223
# a = list(input('请输入：'))
# if a == a[::-1]:
#     print(True)
# else:
#     print(False)


#1.3 字符串切割          ['hello', 'world', 'yoyo']
s = 'hello_world_yoyo'
b = s.split("_")
print(b)

#1.4 拼接字符串          hello_world_yoyo
a = ['hello', 'world', 'yoyo']
print("_".join(a))

#1.5 替换字符            We%20are%20happy.
s = 'We are happy'
a = s.replace(' ','%20')
print(a)


#1.6 九九乘法表
a = range(1,10)
for i in a:
    j = 0
    while j < i:
        j += 1
        print('{j} * {i} = {t}'.format(j=j,i=i,t=j*i),end=' ')
    print()


#1.7  “welcome” 在 字符串”Hello, welcome to my world.” 中出现的位置，找不到返回-1
s = 'Hello, welcome to my world'
b = s.find('welcome')
print(b)


def test():                    #第二种
    a1 = 'Hello, welcome to my world'
    b1 = 'welcome'
    if b1 in a1:
        return a1.find(b1)
    else:
        return -1
print(test())


#1.8 字母w出现的次数
a = 'Hello, welcome to my world'
b = a.count('w')
print(b)
c = a.count('my')
print(c)

#1.9输入一个字符串str, 输出第m个只出现过n次的字符，如在字符串 gbgkkdehh 中,
#找出第2个只出现1 次的字符，输出结果：d
def test1(str1,num,counts):
    # 定义一个空数组，存放逻辑处理后的数据
    list = []
    # for循环字符串的数据
    for i in str1:
        # 使用 count 函数，统计出所有字符串出现的次数
        count = str1.count(i, 0, len(str1))
        # 判断字符串出现的次数与设置的counts的次数相同，则将数据存放在list数组中
        if count == num:
            list.append(i)         #把只出现一次的添加到列表中
    # 返回第n次出现的字符串
    return list[counts - 1]
print(test1('gbgkkdehh',1,2))

#1.11 判断字符串 a 是否包含单词 b ,包含返回True，不包含返回 False
def test2():
    a = 'welcome to my world'
    b = 'world'
    if b in a :
        return True
    else:
        return False
print(test2())


#1.12 输出指定字符串A在字符串B中最后出现的位置,如果B中不包含A,则输出-1
def test3():
    A = 'hello'
    B = 'hi how are you hello world, hello yoyo !'
    if A in B:
        return B.find(A)
    else:
        return -1
print(test3())

#1.13 给定一个数a，判断一个数字是否为奇数或偶数
def test4(num):
    if num % 2 == 0:
        return '偶数'
    else:
        return '奇数'
print(test4(10))


#1.14 输入一个姓名，判断是否姓王
# def test5():
#     a = input('请输入姓名')
#     if a[0] =='王':
#         return '用户姓王'
#     else:
#         return '用户不姓王'
# print(test5())

#1.15 如何判断一个字符串是不是纯数字组成
def test6(num):
    if num.isdigit() == True:
        return '是纯数字'
    else:
        return '不是纯数字'
print(test6('123345A'))

#1.16全部转成大写
a = 'This is string example….wow'
b = a.upper()
print(b)

#1.16 全部转成小写
a = 'Welcome To My World'
b = a.lower()
print(a)

#1.17 首尾空格去掉
a = '  welcome to my world   '
b = a.strip()
print(b)
#1.18 左边的空格去掉
a = '  welcome to my world ！'
b = a.lstrip()
print(b)

#1.19 右边的空格去掉
a = '  welcome to my world !  '
b = a.rstrip()
print(b)

#1.20 所有空格都去掉
a = '  welcome to my world !  '
b = a.replace(' ','')
print(b)

#1.21 去重后排序
s = 'ajldjlajfdljfddd'
listA = []
for i in s:
    if i in listA:
        listA.remove(i)
        listA.append(i)
    else:
        listA.append(i)
listA.sort()
print("".join(listA))


#1.22 去重保留原来的顺序，输出”adfjl”
def test7():
    s = 'ajldjlajfdljfddd'
    list = []
    for i in s:
        if i in list:
            list.remove(i)        #先把列表中的i全部删除
        list.append(i)            #再添加一个 i
    #a = list.sort()           #sort排序使用在列表
    a = sorted(list)        #sorted 使用在函数方法内
    return "".join(a)
print(test7())


#1.23 打印菱形图案
def test():
    n = 8
    for i in range(-int(n/2), int(n/2) + 1):
         print(" "*abs(i), "*"*abs(n-abs(i)*2))
print(test())


#1.24 输出一个正数判断是几位数,且逆序打印
a = input("请输入一个正数")
print(len(a))
b = list(a)
b.reverse()                #翻转字符串
print("".join(b))