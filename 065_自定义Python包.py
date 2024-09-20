# Python包文件夹 包含一堆python模块和__init__.py
import related_data.my_package.my_module1
import related_data.my_package.my_module2

related_data.my_package.my_module1.print1()
related_data.my_package.my_module2.print2()

from related_data.my_package import my_module1
from related_data.my_package import my_module2
my_module1.print1()
my_module2.print2()

from related_data.my_package.my_module1 import print1
from related_data.my_package.my_module2 import print2
print1()
print2()

# 在包中添加__init_.py才能表示这是个python包，否则只是普通文件夹
# 在__init_.py中定义all变量 控制*选择的模块
from related_data.my_package import *
my_module1.print1()
# // my_module2.print2()