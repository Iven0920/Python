import related_data.my_module1 as my_module1
my_module1.test(1, 2)

from related_data.my_module1 import test
test(1, 2)

# 同名功能后一个覆盖前一个
from related_data.my_module1 import test
from related_data.my_module2 import test
test(1, 2)

# 当自己运行时name=main 当被其他程序调用时则不是 不执行  便于测试自定义模块文件
# if __name__ == '__main__':
#     test(1, 2)

# 如果在module模块里定义了__all__ = ['test'] 则import * 只会导入all变量里的函数  但其他手动导入方法都可以 e.g import test_1
from related_data.my_module1 import *
test(1, 2)
# test_1(1, 2)