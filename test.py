# def a():
#     return 500
#
# def b():
#     return 500

# a = ["10000"]
# b = ["10000"]
# if (a is b):
#     print("是相同的")
# else:
#     print("是不同的")


#其他资料学习

'''
#使用Faker随机生成伪数据     需要进行安装 pip install Faker
from faker import Faker
fake = Faker(locale='zh_CN')         #设置输出为中文
# fake = Faker()
name = fake.name()
print(name)  # 英文名
address = fake.address()
print(address)
tel = fake.phone_number()
print(tel)


#输出1-100 且移除每次循环的第三位         相当于是移除3的倍数      使用while
a = list(range(1,101))      # a 生成为一个 1-100 的列表
n = 3
i = n
while i <len(a):
    a.remove(a[i-1])
    i = (i - 1) + n
print(a)
'''


#输出1-100  是移除3的倍数       使用for
a = list(range(1,101))
for i in a:
    if i % 3 == 0:
        a.remove(i)
else:
    print(a)






#输入：”MyNameIsTom”       输出：”yMemaNsImoT”
a = "MyNameIsTom"
aa = []
s = ""
for i in a:
    if i.isupper():
        # 如果是大写
        if len(s) == 0:
            s += i
        else:
            aa.append(s)
            s = ''
            s += i
    else:
        s += i
if len(s) > 0:
    aa.append(s)

print(aa)
                # 对列表单词反转并大小写反转
result = []
for j in aa:
    reverse_j = j[::-1]             # j[::-1] 实现字符串翻转
    result.append(reverse_j)
print("".join(result)) # yMemaNsImoT


s = 'MyNameIsTom'
result = []
a = ''
for i in s:
    if i.isupper():
        if len(a) == 0:
            a += i
        else:
            result.append(a)
            a = ''
            a += i
    else:
        a += i
if len(a) > 0:
    result.append(a)
print(result)


#只删除两个相邻的字母
# S = 'abbaca'
# st = []
# for i in S:
#     if len(st) == 0:        #判断数组为空时
#         st.append(i)
#     elif i == st[-1]:       # 判断 i 等于数组最后一个元素时
#         st.pop()
#     else:                   #其他条件
#         st.append(i)
# print("".join(st))          # "".join()  拼接字符转



# 相同相邻的字符一起消掉
z = 'abcccbxezzzrf7788fn'          #axern
results = []
k = ''
for i in z:
    if len(results) == 0:
        results.append(i)
    else:
        if i == k:
            continue
        elif i == results[-1]:
            k = results.pop(-1)
        else:
            results.append(i)
print(''.join(results))


#for循环中嵌套for循环
for n in range(2, 10):
    for x in range(2, n):
        print(x)
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

#队列插入一条数据
a = [1,3,5,7]
a.insert(2,a[0])
a.remove(a[0])
print(a)

#格式化输出   %d 输出整数
a = 55
print("%d"%a)       #直接输出整数a
print("%4d"%a)      #向右对齐，占4个字符，不足填充空格
print("%04d"%a)     #向右对齐，占四个字符，不足填补0
print("%-4d"%a)     #负号表示左对齐，占4个字符，不足填充空格
print("%6.4d"%a)    #向右对齐，不足填补0，  6.4 表示占6个字符，补填后显示4个位数，原数超过四位，显示原数


#格式化输出   %d 输出浮点数
b = 3.1415926
print("%f"%b)       #右对齐，输出浮点数，默认显示6位
print("%.3f"%b)     #右对齐，四舍五入保留三位小数
print("%6.3f"%b)    #右对齐，四舍五入，占位为6，小数保留3位不足补空格




#三位数的水仙花数
sxh = []
for i in range(100, 1000):
    s = 0
    m = list(str(i))
    for j in m:
        s += int(j)**len(m)
    if i == s:
        print(i)
        sxh.append(i)
print("100-999的水仙花数：%s" % sxh)





# x = int(input('请输入第一个数：'))
# y = int(input('请输入第二个数：'))
# z = int(input('请输入第三个数：'))
# # if x > y:
# #     x,y = y,x
# # if x > z:
# #     x,z = z,x
# # if y > z:
# #     y,z = z,y
# # print('输出排序列表未：',x,y,z)
#
# lists = [x,y,z]
# lists.sort()
# print(lists)


#由四个数字组成不同的三位数
count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i!=k and j!=k:
                count += 1
                print(i*100 + j*10 + k)
print('符合总共个数为：',count)


list = [12,34,66,7,88,8,80]
list1 = []
for i in list:
    list1.append(i)
list1.sort()
print(list1)



