# 变量作用域即变量作用范围 局部变量（在函数体内部临时保存数据 当函数调用完成后 销毁局部变量）和全局变量
def test_a():
    num = 100
    print(num)
test_a()
# 出了函数体 局部变量无法使用
# // print(num)

# 全局变量
num = 100
def test_a():
    print(num)
test_a()
def test_b():
    print(num)
test_b()

# 在函数内修改全局变量
num = 100
def test_a():
    print(num)
test_a()
def test_b():
    num = 200 # 局部变量
    print(num)
test_b()
print(num) # 外面的不修改

# global关键字 在函数内部声明变量为全局变量
num = 100
def test_a():
    print(num)
test_a()
def test_b():
    global num
    num = 200 # 全局变量
    print(num)
test_b()
print(num) # 外面也修改了