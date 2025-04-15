#学员信息包含：姓名、性别、手机号
class Student():
    def __init__(self,name,age,mobile):
        self.name = name
        self.age = age
        self.mobile = mobile

    def __str__(self):
        return f'{self.name},{self.age},{self.mobile}'