def test(a, b):
    print(a + b)

def test_1(a, b):
    print(a - b)

# 当自己运行时name=main 当被其他程序调用时则不是 不执行
if __name__ == '__main__':
    test(1, 2)