# 使用对象组织数据
# 1.设计类（设计表格）
class Student:
    name = None
    gender  = None
    nationality = None
    native_place = None
    age = None

# 2.创建对象（打印一张登记表） stu_1既是变量又是类的对象
stu_1 = Student()

# 3. 对像属性赋值（填写表单）
stu_1.name = "Iven"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "四川省"
stu_1.age = 22

# 4. 获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)
