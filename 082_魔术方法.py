# 魔术方法 Python类内置的方法
# 1. __inti__ 构造方法
# 2. __str__ 字符串方法 输出类对象时使用将 类对象转为字符串输出   不加此方法直接print对象会显示对象内存地址
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Student类对象，name:{self.name}，age:{self.age}"

stu = Student("Iven", 22)
print(stu)
print(str(stu))

# 3. __lt__  小于符号比较方法（大于）
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Student类对象，name:{self.name}，age:{self.age}"
    
    def __lt__(self, other):
        return self.age < other.age

stu1 = Student("Iven", 22)
stu2 = Student('Rosenn', 25)
print(stu1 < stu2)
print(stu1 > stu2)

# 4. __le__  小于等于符号比较方法（大于等于）
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Student类对象，name:{self.name}，age:{self.age}"
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __le__(self, other):
        return self.age <= other.age

stu1 = Student("Iven", 22)
stu2 = Student('Rosenn', 22)
print(stu1 < stu2)
print(stu1 > stu2)

# 若未调用eq方法 则默认比较内存地址
print(stu1 == stu2)

# 5. __eq__  比较运算符比较方法（大于等于）

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Student类对象，name:{self.name}，age:{self.age}"
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __le__(self, other):
        return self.age <= other.age
    
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("Iven", 22)
stu2 = Student('Rosenn', 22)
print(stu1 == stu2)