# module
# [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]      []可选

# import 导入
# python 内置time.py 这个文件
import time
print("你好")
time.sleep(5)  # 通过.可以使用模块内部的全部功能（类、函数、变量）
print("我好")

# from 模块名 import 功能名  针对某个功能去使用
from time import sleep
print("你好")
sleep(5)  # 可以直接调用sleep
print("我好")

# 使用 * 导入模块所有功能 并可以直接调用 
from time import *
print("你好")
sleep(5)  # 可以直接调用sleep
print("我好")

# as 别名
import time as t
print("你好")
t.sleep(5)  # 可以直接调用sleep
print("我好")

from time import sleep as sl
print("你好")
sl(5)  # 可以直接调用sleep
print("我好")