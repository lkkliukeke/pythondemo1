
#数据结构

#列表：列表是可以修改的，字符串和元组不能修改
#将列表当做堆栈使用  append()方法可以把一个元素添加到堆栈顶。 pop()方法，把一个元素从堆栈顶释放出来
stack = [1,2,3,4,5]
stack.append(6)
stack.append(7)         #添加到堆栈顶
print(stack)
stack.pop()             #将一个元素从堆栈顶移除
print(stack)

#列表当队列使用
from collections import deque
queue = deque(['runoob','baidu','taobao'])
queue.append('Goodle')
queue.append('jingdong')
print(queue)
print(queue.popleft())         #从左边开始移除
print(queue)


#列表推导式
list1 = [1,2,3,4,5,6,7,8]
list1_new = [i * i for i in list1]
print('1，列表推导式值为：',list1_new)

#列表推导式
var1 = [2,4,6]
var2 = [3,5,7]
list_var = [x*y for x in var1 for y in var2]
print('2，列表推导式',list_var)


#函数类型
list1 = [1,2,3,4,5,6,7,8]
def list2(val):
    return val * val
list2_new = [list2(i) for i in list1]
print('2，列表推导式值为：',list2_new)


#嵌套列表解析
matrix = [[1,2,3,4],[4,5,9,7],[6,7,8,1]]
str = [[row[i] for row in matrix] for i in range(4)]
print('3，列表推导式为：',str)




#元组和序列    由若干逗号分隔的值组成的
t = 123,34657,9867
print(t)
print(t[0])
u = t,('aaa','bbb','ccc')     #两个元组合成的
print(u)



#集合

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

#字典推导式      构造函数
var3 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print('字典推导式1',var3)               #返回的是组合类型 key 和 value


#字典推导式
var4 = {x: x**2 for x in (2, 4, 6)}
print('字典推导式2：',var4)

#有去重功能
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


#字典遍历时，关键字和对应值同时解读出来                          items()
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
    print(k)


#序列遍历时，可以同时得到索引位置和对应的值                        enumerate()   方法写在括号内
for i, v in enumerate(['name','age','sex']):
    print(i,v)

#同时遍历两个或更多的序列                                       zip()
que1 = ['name','age','sex']
que2 = ['red','blue','pink']
for v,n in zip(que1,que2):
    print('what is your {0}? It is {1}.'.format(v,n))


#反向遍历一个序列                                            reversed()
for i in reversed(range(5)):
    print('反向遍历后：',i)

#按顺序遍历一个序列，返回一个已排序的序列                         sorted()
varque = ['orange','banana','apple','pear']
for i in sorted(varque):
    print('按顺序排列后的：',i)







#模块
#引入python标准库中的sys.py模块
#sys.argv 是一个包含命令行参数的列表
#sys.path 包含了一个python解释器自动查找所需模块的路径的列表

import sys           #引入python标准库中的sys.py模块
print('命令行参数如下：')
for i in sys.argv:          #sys.argv 是一个包含命令行参数的列表
    print('打印模块',i)

print(sys.path)

def print_func( par ):
    print('hello')
    return


# import support
# support.print_func('runoob')


def fib(n):  # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

