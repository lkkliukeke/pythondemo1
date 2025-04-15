from student import *
class StudentManager(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        #加载数据
        self.load_student()
        self.show_menu()
        #显示功能菜单
        while True:
            #用户输入功能序号
            menu_num = int(input('请输入要操作的序号：'))
            #根据用户的输入的序号执行不同的功能
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break


    def load_student(self):
        pass
    @staticmethod
    def show_menu():
        print('请选择一下功能......')
        print('1：添加学员')
        print('2：删除学员')
        print('3：修改学员信息')
        print('4：查询学员信息')
        print('5：显示所有学员信息')
        print('6：保存学员信息')
        print('7：退出系统')

    #添加学员信息
    def add_student(self):
        #输入学员信息
        name = input('请输入学员姓名:')
        age = input('请输入学员年龄：')
        mobile = input('请输入学员手机号：')
        #实例化对象
        student = Student(name,age,mobile)
        #将学员信息添加到列表中
        self.student_list.append(student)
        print(student)
        # print(self.student_list)
    #删除学员信息
    def del_student(self):
        #请输入要删除学员的姓名
        del_name = input('请输入要删除学员信息的姓名')
        for i in self.student_list:
            #遍历学员列表
            if i.name == del_name:
                self.student_list.remove(i)
                break
            else:
                print('未找到此人')
            print(self.student_list)
    #修改学员信息
    def modify_student(self):
        #请输入要修改学员信息的姓名
        modify_name = input('请输入要修改的学员姓名：')
        #遍历学员列表
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('请输入修改后的姓名：')
                i.age = input('请输入修改后的年龄：')
                i.mobile = input('请输入修改后的手机号：')
                print(f'修改改学员信息成功，姓名为：{i.name}，年龄为：{i.age},手机号为：{i.mobile}')
                break
            else:
                print('未查到学员信息')
    #查询学员信息
    def search_student(self):
        #输入查询学员信息的姓名
        search_name = input('请输入要查询学员的姓名：')
        #遍历学员列表
        for i in self.student_list:
            if i.name == search_name:
                print(f'查到学员信息为：姓名：{i.name}，年龄为：{i.age}，手机号为：{i.mobile}')
                break
            else:
                print('未查到学员信息')
    #查询所有学员
    def show_student(self):
        #遍历学员列表
        for i in self.student_list:
            print(f'学员的信息为：姓名：姓名：{i.name}，年龄为：{i.age}，手机号为：{i.mobile}')
    #保存学员信息
    def save_student(self):
        pass
        #打开文件
        # f = open('student.data','w')