# 类的定义和使用
# class 类名称: 类的属性（成员变量） 类的行为（成员方法）
# 函数：类外部的函数 方法：类内部的函数

class Student():
    name = None
    # 在成员方法中访问成员变量 加self
    # def (self) self就是类对象本身
    def say_hi(self):
        print(f"大家好！我是{self.name}")
    
    # 在成员方法中访问外部传入的变量 不需要self
    def greet(self, msg):
        print(f"大家好，我是{self.name}, {msg}")

stu_1 = Student()
stu_1.name = "Iven"
# self自动传入 可当作不存在 无需理会
stu_1.say_hi()
stu_1.greet("哈哈哈哈")

stu_2 = Student()
stu_2.name = "Rosenn"
# self自动传入 可当作不存在 无需理会
stu_2.say_hi()