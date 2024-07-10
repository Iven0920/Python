# 1.位置参数 调用函数时根据函数定义的参数位置来传递函数
def user_info(name, age, gender):
    print(f"姓名是:{name}，年龄是：{age}，性别是{gender}")
user_info('Iven', 22, '男')

# 2.关键字参数 函数调用时你用键 = 值 形式来传递参数  参数位置可以并不固定 
# * 也可以混用 但混用时必须把位置参数放在关键词参数前面
user_info(age=22, gender='男', name='Iven')
user_info(gender='男', name='Iven', age=22)
user_info('Iven', gender='男', age=22)
# // user_info(name='Iven', '男', age=22)

# 3.缺省参数 为参数提供默认值
# * 默认值参数必须写在最后面
def user_info(name, age, gender='男'):
    print(f"姓名是:{name}，年龄是：{age}，性别是{gender}")
# // def user_info(name='iven', age, gender):
# //     print(f"姓名是:{name}，年龄是：{age}，性别是{gender}")
user_info(age=21, name='Rosenn')
user_info(age=21, name='Rosenn', gender='女')

# 4.不定长参数 可变参数 不确定调用时会传递多少参数 也可以不传递参数 
# 位置传递 *args 传递一个元组类型 一般叫args
def user_info(*args):
    print(f"args参数的类型是：{type(args)}，内容为{args}")
user_info(1, 2, 3, 'Iven', {'hello'})
# 关键字传递 **kwargs 键值 传递一个字典
def user_info(**kwargs):
    print(f"kwargs参数的类型是：{type(kwargs)}，内容为{kwargs}")
user_info(name='Iven', age=22, score=93, word={'hello'})