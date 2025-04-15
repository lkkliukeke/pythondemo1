#学员信息列表
info = [{'name':'Tom', 'age':18, 'mobile':'13578664321'}, {'name':'Mary', 'age':18, 'mobile':'19920187732'}, {'name':'Jennifier', 'age':18, 'mobile':'18862357791'}]
#添加学员信息
def add_info():
    name1 = input('您输入的姓名为：')
    age1 = int(input('您输入的年龄为：'))
    mobile1= input('您输入的电话号码为：')
    #表明被其修饰的变量是全局变量
    global info
    for i in info:
        if name1 == i['name']:
            print('该用户已存在')
            return
    dict_new = {}
    dict_new['name'] = name1
    dict_new['age'] = age1
    dict_new['mobile'] = mobile1
    info.append(dict_new)
    print(info)
    print('添加成功')
add_info()

#删除学员
def del_info():
    del_name = input('请输入删除人员的姓名:')
    global info
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('删除人员不存在')
    print(info)
    print('删除成功')
del_info()

#修改成员
def upd_info():
    upd_name = input('请输入修改人员的名字：')
    global info
    for i in info:
        if upd_name == i['name']:
            i['mobile'] = '15290179035'
            break
    else:
        print('未查询到此人')
    print(info)
    print('修改成功')
upd_info()

#查询人员
def seaech_info():
    search_name = input('请输入要查询人员的姓名：')
    global info
    for i in info:
        if search_name == i['name']:
            print('查找到的学员信息如下：——————————————')
            # print("查询到的人员姓名为："+i['name'],"年纪为："+i['age'],"电话号为："+i['mobile'])
            print(f"查询到的人员姓名为{i['name']},年纪为{i['age']},电话号为{i['mobile']}")
            break
    else:
        print('未查到此人')
seaech_info()

#遍历人员信息
def all_info():
    print('开始打印所有人信息：————————————————')
    global info
    for i in info:
        print(f"人员姓名为{i['name']},年纪为{i['age']},电话为{i['mobile']}")
all_info()