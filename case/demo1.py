# coding=utf-8
#打印
print("hello word")
print("你好")

#判断语句
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")


# 代码拼接换行 \
item_one=1
item_two=2
item_three=3
total = item_one +\
        item_two +\
        item_three
print(total)
print(item_three)

# raw_input("按下enter键退出，其他任意键显示 \n")

# 执行结果换行\n
x = 'runoob'
b = "你很棒"
print(x + '\n' + b)
print(r'x\nb')     #放在一行内显示的

#赋值多种方法
a = b = c = 1
print (a,b,c)
a,b,c=1,2,3
print(a,b,c)


# 执行删除语句
var1 = "你好吗？"
var2 = 10
# del var1  #执行删除一个对象
# del var1,var2  #执行删除多个对象
print(var1)
print(var2)

# 字符串截取 [头下标：尾下标]  从左到右下标从0开始，右-左：下标从-1开始   左闭右开
s = "abcdefg"
print(s[1:3])  #截取下标为1至3之间的
print(s[0])    #截取下标为0的
print(s[3:])    #截取下标为3之后的
print(s * 2)    #连续输出两次
print(s + "hello")   #输出连接的字符串
print('s\nhello')     #此时的\n为换行
print(r's\nhello')     #此时为输出\n

# 截取接收三个参数  1-为第一个头下标，6-为尾下标，2-为设置截取的间隔（从前一个截取的往后数第二个）
str=["a","b","c","d","e","f"]
print(s[1:6:2])


# 列表使用[]标识   元素类型可以不相同  列表支持修改元素
demo1=["1","2",567,"000"]
print(demo1)
print(demo1[1:3])     #列表截取最后一个坐标前一位数  ['2','567']
demo1[2]="1000"   #列表使用是合法的
print(demo1)

# 元组使用()标识     元素类型可以不相同       元组不支持修改元素   一个元素后需要加逗号
demo2=("999",666,"nihao")
print(demo2)
#demo2[2]=1000  #元组无法使用赋值修改
print(demo2)
print(demo1)

print('\n')
# set（集合）  可进行运算  重复的只输入一个
a = set('abracadabra')
b = set('alacazam')

print(a)
print('\n')
print(b)
print(a-b)     #求a和b的差集 保留a
print(a | b)   #求a和b的并集
print(a & b)   #求a和b的交集
print(a ^ b)   #求a和b中不同时存在的元素


# 字典使用{}标识，由key和value组成   key必须是唯一的
demo3={"name":"zhangsan","code":666278,"sex":"男"}
print(demo3)
 #添加
dict = {}
dict['one'] = "1 - 菜鸟教程"     #  ’one‘是key  ‘1-菜鸟教程’是value
dict[2] = "2 - 菜鸟工具"
print(dict)

dict = {'one': '1-菜鸟教程', 2: '2-菜鸟教程'}
print(dict.keys())      #输出所有的键 key
print(dict.values())     #输出所有的值  values

# 字符间的转换
x=5.9
print(x)
# float(x)
# str(x)
int(x)

# 运算符:算术运算符，比较运算符，赋值运算符，位运算符，逻辑运算符，成员运算符，身份运算符，运算符优先级
# 逻辑运算符 and:与--a and b     or:或--a or b      not:非--not a
# 成员运算符    in:指在指定序列值找到值返回       ont in:在指定序列中没有找到值返回
# 身份运算符    is:判断两个标识符是不是引用自一个对象     is not:判断两个标识符是不是引用自不同对象
# 算术运算符 +  -   *   /   %(取模，除法余数）  //(取整数，返回上的整数部分，向下取)
a=21
b=10
c=0
# c=a/b
c=a%b
print(c)
a = 2
b = 3
c = a**b
print(c)

# 成员运算符
list = {'helloA','helloB','nohello','like','door'}
if 'helloA' in list:
    print('helloA 在集合中')
else:
    print('helloA 不在集合中')


# 判断语句
a = 21
b = 10
if a == b:
    print("1. a等于b")
else:
    print("1,  a不等于b")






# 身份运算符 is
a = ["1000"]
b = ["1000"]
if (a is b):
    print("是相同的")
else:
    print("是不同的")

print(id(a))
print(id(b))




# 条件语句 if  else
a = 1
while a < 7:
    if (a % 2 == 0):
        print(a,"is 结果1")
    else:
        print(a,"is 结果2")
    a += 1
print(a)


flag = False
name = "luren"
if name == "luren":
    flag = True
    print(flag)
    print("hello")
else:
    print(name)


# 条件语句 if  elif   else
a = 4
if a == 1:
    print(a,"is 结果1")
elif a == 2:
    print(a,"is 结果2")
elif a == 3:
    print(a, "is 结果3")
else:
    print("nihao")


# 写在一行内的显示
print('nihaoma')
import sys; x = 'runoob'; sys.stdout.write(x + '\n')


# 用于判断数据类型
a = 123
print(type(a))               #查看数据类型
print(isinstance(a,int))     #判断数据类型


#and优先级高于or
x = True
y = False
z = False

if x or y and z:
    print("yes")
else:
    print("no")


#截取字符串
var1 = 'hello world'
print(var1[0:6])

#格式化字符串  f-string     语法f'{转换变量}'
name = 'runoob'
print(f'hello {name}')        #格式化字符串
# print('hello'+'name')        拼接字符串
x = 1
print(f'{x+1}')          #进行计算
print(f'{x+1=}')         #  =用来拼接运算表达式






