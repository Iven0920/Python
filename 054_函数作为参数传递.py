# 计算逻辑的传递 而非数据传递
def test_func(compute):
    result = compute(1, 2)
    print(f"compute参数的类型是：{type(compute)}，计算结果:{result}")

def compute(x, y):
    result = x + y
    return result

test_func(compute)