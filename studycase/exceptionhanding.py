#异常 模块  与包

import time

# #打开一个不存在得文件
# f = open('ceshi.txt','r')


#异常捕捉的方法
#捕获常规异常
# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码
try:
    f = open('ceshi.txt','r')
except:
    f = open('ceshi.txt','w')


#捕获置指定异常
#如果尝试执行代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
try:
    print(name)
except NameError:
    print('name变量名称未定义错误')


#捕获多个异常
#捕获多个异常时，可以把要捕获异常类型的名字  放到except后面，并使用元组的方式进行书写
try:
    print(1/0)
except (NameError,ZeroDivisionError):
    print('这边的错误是。。。。')


#捕获异常并输出描述信息
try:
    print(num)
except (NameError,ZeroDivisionError) as e:
    print(e)



#捕获所有异常
try:
    print(name)
except Exception as e:
    print(e)


#异常else
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('我是else，是没有异常时候执行的代码')



#异常的finally
#finally表示是否异常都要执行的代码，例如关闭文件
try:
    f = open('ceshi.txt','r')
except Exception as e:
    f = open('ceshi.txt','w')
else:
    print('没有异常会执行')
finally:
    f.close()




print('--------异常综合案例---------')
try:
    f = open('D:\File\文档\新建文本文档.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content,end='')
    except:
        #若在读取文件时发生异常，则会捕捉到
        print('读取时发生了异常')
    finally:
        f.close()
        print('关闭文件')
except:
    print('没有这个文件')




# print('------抛出自定义异常---------')
#抛出自定义异常的语法为 ’raise异常类对象‘
# class ShortInputError(Exception):
#     def __init__(self,length,min_length):
#         self.length = length
#         self.min_length = min_length
#
#     def __str__(self):
#         return f'您输入的密码长度未{self.length}位，不能少于{self.min_length}个字符'
#
# def main():
#     try:
#         password = input('请输入您的密码：')
#         if len(password) < 6:
#             raise ShortInputError(len(password),6)
#     except Exception as e:
#         print(e)
#     else:
#         print('密码输入完成')
# main()





#模块
#模块的导入方式
# import 模块名
# from 模块名 import 功能名
# from 模块名 import*
# import 模块名 as 别名
# from 模块名 import 功能名 as 别名


#模块名
# import 模块名
# import 模块名1,模块名2
print('--------模块--------')
import math
print(math.sqrt(9))


# from 模块名 import 功能名
# 功能名()
# from os import mkdir
# mkdir('image')


# from 模块名 import*
from sys import*
print(platform)


#import 模块名 as 别名
import time as tt
tt.sleep(2)
print('hello')

#from 模块名 import 功能 as 别名
from time import sleep as sl
sl(2)
print('nihao')




#制作自定义模块
#创建一个文件 python文件，  命名为  my_module1.py
# def test(a,b):
#     print(a+b)
# test(1,2)
# # 只在当前文件中调用该函数，其他导入的文件内不符合该条件，则不执行testA函数调用
# if __name__ == '__main__':
#     test(1,4)

#调用方式
# import my_module1


#创建一个新的文件my_module1.py
# def test1(a,b):
#     print(a+b)
# # 创建一个新的文件my_module2.py
# def test1(a,b):
#     print(a-b)

# 导入模块和调用功能代码
# from my_module1 import test1
# from my_module2 import test1
# test1函数是模块2中的函数
# test1(1, 1)