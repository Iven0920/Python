# 属性成员变量的赋值
# 构造方法 __init__()
# 在创建类对象（构造类）的时候，会自动执行
# 在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用

class Student:
    # 这里可以不写成员变量
    # name = None
    # age = None
    # tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个对象")

stu = Student("Iven", 22, 18744440367)
print(stu.name)
print(stu.age)
print(stu.tel)

# 练习
class Student:
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

# * 定义一个list用来存储10个学生信息对象
stu_list = []
for i in range (10):
    print(f"当前录入第{i + 1}位学生信息，总共需要录取10位同学")
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    place = input("请输入学生地址：")
    stu = Student(name, age, place)
    stu_list.append(stu)
    print(f"学生{i + 1}信息录入完成，信息为【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.place}】")

print(stu_list)