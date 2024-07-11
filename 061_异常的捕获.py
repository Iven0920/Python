# 捕获异常：提前假设某处出现异常，做好提前准备，当真的出现异常，可以有后续手段
# 基本捕获异常方法 try... except 捕获所有异常
try:
    f = open("related_data/error.txt", "r", encoding="UTF-8")
except:
    print("出现异常了，文件不存在，将以w模式打开，自动创建文件")
    f = open("related_data/error.txt", "w", encoding="UTF-8")

# 捕获指定异常  
try:
    # print(name)
    1 / 0
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

# 捕获多个异常
try:
    print(1 / 0)
    # print(name)
except (NameError, ZeroDivisionError) as e:
    print("ZeroDivision错误")

# 捕获所有异常 Exception 也可以直接用最基本的异常
try:
    # print(name)
    1 / 0
    # f = open("related_data/all_error.txt", "r", encoding="UTF-8")
except Exception as e:
    print("出现异常了")

# 异常else 没有异常执行 可选
try:
    # print(name)
    # 1 / 0
    # f = open("related_data/all_error.txt", "r", encoding="UTF-8")
    print("hello")
except Exception as e:
    print("出现异常了")
else:
    print("没有异常！")

# 异常finally 无论是否异常都执行 可选
try:
    f = open("related_data/error.txt", "r", encoding="UTF-8")
except Exception as e:
    print("出现异常了")
    f = open("related_data/error.txt", "w", encoding="UTF-8")
else:
    print("没有异常！")
finally:
    print("我是finally，有没有异常我都要执行")
    f.close()