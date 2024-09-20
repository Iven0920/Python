import random, json
# 类型注解  在代码涉及数据交互的地方，提供数据类型的注解 协助IDE对数据类型进行提示或开打发着自身做类型的备注
# 一般只会在一眼看不出来的代码里去注释 
# todo 变量类型注解 变量:类型 
# 1.基础数据类型注解 
val_1: int = 18
var_2: str = "Iven"
var_3: bool = True

# 2.类对象型注解 
class Student:
    pass
stu: Student = Student()

# 3.基础容器类型注解 
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"Iven", 22}

# 4.容器类型详细注解（元组注释要将每一个元素标记 字典注释要2个类型 key value）
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, '2', True)
my_dict: dict[str, int] = {"Iven", 22}

# todo 在注释中进行类型注解 type: int
val_1 = random.randint(1, 10) # type: int
val_2 = json.loads('{"name": "Iven"}') # type: dict[str, str]
def func():
    return 10
val_3 = func() # type: int

# 类型注释只是提示性的 写错不会报错
val_4: int = 'Iven'
val_5: str = 123