
#公众号小学数学练习题


#2.1 三位数的水仙花数
#abc = a**3 + b**3 + c**3
str1 = []
s = range(100, 1000)
for i in s:
    k = 0
    b = str(i)              #int类型转为str
    a = list(b)             #str类型转为list列表
    m = list(a)
    for j in m:
        k += int(j)**3
    if k == i:
        print(i)
        str1.append(i)
print('水仙花数为：',str1)


#2.2 完整数     暂时没有完成
# rand = range(1,1001)
# stad = range(1,1001)
# lists = []
# for i in rand:
#     tmp = []
# for j in stad:
#     if j:
#         if not i%j:
#             tmp.append(j)
#         else:
#             continue
#     else:
#         break
#     count = sum(tmp)
#     if count == i:
#         tmp.append(i)
#     else:
#         continue
# print(lists)


#2.3 数字1-100求和
a = range(1,101)
s = 0
for i in a:
    s +=i
print(s)


#2.5 计算求1+2-3+4-5… …100的值
rand = range(1,101)
s = 1
k = 0
for i in rand:
    if i%2 == 0:
        # print(i)
        s += i
    if i%2 != 0:
        # print(i)
        k += i
        n = k-1
sum = s - n
print(s)
print(n)
print(sum)

#2.4 计算求1-2+3-4+5-…-100的值
rand = range(1,101)
a = 0
b = 0
for i in rand:
    if i%2 == 0:
        # print(i)
        a += i
        k = -a
        # print(a)
    if i%2 != 0:
        b += i
        # print(b)
sum1 = k + b
print(k)
print(b)
print(sum1)

#2.6 计算 1-n 之间的所有 5 的倍数之和 默认计算 1-100
n = range(1,100)
a = 0
for i in n:
    if i%5 == 0:
        a += i
print('5的倍数和：',a)

#2.7 n个自然数的立方和
a = range(1,60)
lits = []
c = 0
for i in a:
    if len(str(i)) == 2:
        d = str(i)[1]
        if int(d) == 3:
            lits.append(i)
print(lits)
for j in lits:
    c += j
print(c)


#2.8 阶乘10!   10!=10x9x8x7x6x5x4x3x2x1
a = range(1,11)
s = 1
for i in a:
    s = s * i
print('阶乘10！的值为：',s)

#2.9 求1+2!+3!+…+10!的和
a = range(1,11)
lists = []
s  = 1
m = 0
for i in a:
    if i >0:
        s = s * i
        m = m + s
    lists.append(s)
print('阶乘1-10的值：',m)

#2.10 求s=a+aa+aaa+aaaa+aa…a的值    3x10**4+ 3x10**3+ 3x10**2 + 3x10**1 +3x10**0
a = range(6)
s = 0
for i in a:
    s += 3*(10**i)
print(s)


