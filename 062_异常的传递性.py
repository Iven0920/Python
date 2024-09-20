def func1():
    print("func1开始")
    num = 1 /0
    print("func1开始")

def func2():
    print("func2开始")
    func1()
    print("func2开始")

def main():
    # 有传递性 可以在最高一层捕获最底一层出现的异常
    try:
        func2()
    except Exception as e:
        print(f"出现异常，异常信息是：{e}")

main()

# 传递性 由最底一层到最高层
# 发生异常: ZeroDivisionError
# division by zero
#   File "D:\桌面\Coding\Python\062_异常的传递性.py", line 3, in func1
#     num = 1 /0
#           ~~^~
#   File "D:\桌面\Coding\Python\062_异常的传递性.py", line 8, in func2
#     func1()
#   File "D:\桌面\Coding\Python\062_异常的传递性.py", line 12, in main
#     func2()
#   File "D:\桌面\Coding\Python\062_异常的传递性.py", line 14, in <module>
#     main()
# ZeroDivisionError: division by zero