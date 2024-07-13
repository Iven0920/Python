# 对函数（方法）的类型注解  
# 形参注解 def 方法名(形参名:类型, ....)

def add(x: int, y: int):
    return x + y
add()

# 返回值注解 def 方法名(形参名:类型, ....) -> 返回值类型
def func(data: list) -> list:
    return data
func()

# 提示性而非决定性
print(func(1))