# class Cat:
#     def __init__(self, name):
#         self.name = name
#         print('他来了 他来了')
#
#     def __del__(self):
#         print('他走了 他走了')
#
# #  Tom 是一个全局变量
# tom = Cat('Tom')
# print(tom.name)
# print('-' * 50)


# def test_var_args(f_arg,*args):
#     print("first normal arg",f_arg)
#     for arg in args:
#         print("anther arg through *args",arg)
# test_var_args('yasoob','test','python','eggs')


# A1=[1, 'aa', 2, 'bb', 'val', 33]
# def test_place(var,string):
#     if string not in var:
#         return -1
#     else:
#         return A1.index(string)
# print(test_place(A1,'val'))


#getattr()函数用于返回一个对象属性值
class A(object):
    count = 0
    def __init__(self):
        self.name = "yoyo"
        self.age = 18
    def start(self):
        print("start1111111")
a = A()
# 获取属性, 实例方法也是类的属性
print(getattr(a, "count"))
print(getattr(a, "name"))
print(getattr(a, "start"))


#属性拦截器    __getattribute__
class A(object):
    count = 0
    def __init__(self):
        self.name = "yoyo"
        self.age = 18
    def start(self):
        print("start1111111")
    def __getattribute__(self, item):
        """属性拦截器"""
        print("调用了A类的属性:", item)
        return object.__getattribute__(self, item)
a = A()
# A()实例对象属性会调用__getattribute__
print(a.count)
print(a.age)
print(a.name)
print(a.start())




class test(object):
    num = 13
    def __init__(self):
        self.name = 'zhangsan'
        self.phone = 15290179035
    def __getattribute__(self, item):
        print('这是一个拦截器',item)
        return object.__getattribute__(self,item)
a = test()
print(a.name)
print(a.phone)
print(a.num)


# lists = {3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48}
def testnums(lists):
    if len(lists) < 2:
        return lists
    centernum = lists[len(lists) // 2]              #根据列表下标获取中间值
    listleft = []
    listright = []
    lists.remove(centernum)
    for i in lists:
        if i >= centernum:
            listright.append(i)
        else:
            listleft.append(i)
    return sorted(listleft + [centernum] + listright)
print(testnums([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))




def bubble_sort(arr):
    """冒泡排序"""
    # 第一层for表示循环的遍数
    for i in range(len(arr) - 1):
        # 第二层for表示具体比较哪两个元素
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                # 如果前面的大于后面的，则交换这两个元素的位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print(bubble_sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))





def sortcase(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j + 1] = lst[j + 1],lst[j]
    return lst
print(sortcase([3, 44, 38, 5, 47, 15, 36, 26, 27, 2]))