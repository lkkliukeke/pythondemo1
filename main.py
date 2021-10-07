# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#用于移除两个集合都存在的元素                         difference_update(set) set:必需，用于计算差集的集合
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)                                  #移除两个集合都包含的元素
print('移除两个集合都存在的元素：',x)


# def fib(n):  # 定义到 n 的斐波那契数列
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a + b
#     print()


def fib2(n):  # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
print(fib2(10))



# s = '0'
# n = int(s)
# print(type(n))
# print(10/n)

# import pdb
# a = 'aaa'
# print(pdb.set_trace())
# b = 'bbb'
# c = 'ccc'
# final = a+b+c
# print(pdb.set_trace())
# print(final)

#设置断点 使用 pdb.set_trace()   在控制台输入命令进行执行语句
# import pdb
# def combine(s1,s2):
#     s3 = s1 + s2 + s1
#     s3 = '"' + s3 + '"'
#     return s3
# a = 'aaa'
# pdb.set_trace()       #设置断点
# b = 'bbb'
# c = 'ccc'
# final = combine(a,b)
# print(final)




def foo(n1):
    n = int(n1)
    assert n != 0, 'n is zero!'
    return 10/n
def main():
    foo('0')




p = lambda x,y:x+y
print(p(4,6))


def test(x):
    return x*x
print(test(9))



