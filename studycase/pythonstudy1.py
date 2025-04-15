
#练习
def test1():
    print('_'*10)
    print('欢迎登录学生管理系统')
    print('1:添加学员信息')
    print('2:删除学员信息')
    print('3:修改学员信息')
    print('4:查询学员信息')
    print('5:遍历输出学员信息')
    print('6:退出系统')
    print('-'*20)
test1()
while True:
    num_put = int(input('请输入要查询的项目序号：'))
    if num_put == 1:
        print('添加学员信息')
    elif num_put == 2:
        print('删除学员信息')
    elif num_put == 3:
        print('修改学员信息')
    elif num_put == 4:
        print('查询学员信息')
    elif num_put == 5:
        print('遍历学员信息')
    elif num_put == 6:
        choose = input('确定退出系统吗？yes/no')
        if choose == 'yes':
            print('退出系统')
            break
    else:
        print('输入内容错误')





