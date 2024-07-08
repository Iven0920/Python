# 无返回值的函数 返回None这个字面量
def say_hi():
    print("Hi")

result = say_hi()
print(f"无返回值函数，输出的值是{result}，输出值的类型为{type(result)}")

# 主动返回
def say_hi():
    print("Hi")
    return None
result = say_hi()
print(f"无返回值函数，输出的值是{result}，输出值的类型为{type(result)}")

# 在if判断中，None等同于False
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None
result = check_age(16)
# * 只有True才进入if
if not result:
    print("未成年不可以进入")

# None用于声明无初始内容的变量
name = None