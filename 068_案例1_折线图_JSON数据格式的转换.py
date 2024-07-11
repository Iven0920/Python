"""
json 是一种轻量级数据交互格式 可以按照json指定的格式去组织和封装数据 
本质上是一个带有特定格式的字符串 
负责不同编程语言中的数据传递和交互 类似于国际通用语言 
"""

# 格式有两种 一种是字典 另一种是列表嵌套字典
import json

# dumps() 列表转json
# 若传入中文加入ensure_ascii=False 不使用ASCII码 直接传入
data = [{"name":"Iven", "age":"21"}, {"name":"Rosenn", "age":"18"}, {"name":"派大星", "age":"25"}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 字典转json
d = {"name":"Iven", "age":"21"}
json_str = json.dumps(d , ensure_ascii=False)
print(type(json_str))
print(json_str)

# loads() json转列表
s = '[{"name":"Iven", "age":"21"}, {"name":"Rosenn", "age":"18"}, {"name":"派大星", "age":"25"}]'
l = json.loads(s) 
print(type(l))
print(l)

# json转字典
d = '{"name":"Iven", "age":"21"}'
l = json.loads(d) 
print(type(l))
print(l)


