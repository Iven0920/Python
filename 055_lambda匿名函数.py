# def 定义带有名称的函数 可以重复使用
# lambda 定义匿名函数 临时使用一次 lambda 传入参数: 函数体(一行代码) 只限一行代码
def test_func(compute):
    result = compute(1, 2)
    print(f"compute参数的类型是：{type(compute)}，计算结果:{result}")

test_func(lambda x, y: x + y)