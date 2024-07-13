# Union类型 使用Union可以进行联合类型注释 对list、dict、函数存放的不同类型数据进行注释 显示某一数据类型或另一数据类型

from typing import Union
my_list: list[Union[int, str]] =[1, 2, "Iven", "Rosenn"]

def func(data: Union[int, str]) -> Union[int, str]:
    pass
func()