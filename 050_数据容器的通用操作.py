# 1.遍历 for while

# 2.统计
list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)
str1 = "Iven likes apple"
set1 = {1, 2, 3, 4, 5}
dict1 = {'Iven':99, 'rosenn':93, 'Starry':89}
# len 元素个数
print(f"列表 元素个数：{len(list1)}")
print(f"元组 元素个数：{len(tuple1)}")
print(f"字符串 元素个数：{len(str1)}")
print(f"集合 元素个数：{len(set1)}")
print(f"字典 元素个数：{len(dict1)}")

# max 最大元素
print(f"列表 最大元素：{max(list1)}")
print(f"元组 最大元素：{max(tuple1)}")
print(f"字符串 最大元素：{max(str1)}")
print(f"集合 最大元素：{max(set1)}")
print(f"字典 最大元素：{max(dict1)}")

# min 最小元素
print(f"列表 最小元素：{min(list1)}")
print(f"元组 最小元素：{min(tuple1)}")
print(f"字符串 最小元素：{min(str1)}")
print(f"集合 最小元素：{min(set1)}")
print(f"字典 最小元素：{min(dict1)}")

# 3.容器转换功能 
# 转列表
print(f"列表 转列表：{list(list1)}")
print(f"元组 转列表：{list(tuple1)}")
print(f"字符串 转列表：{list(str1)}")
print(f"集合 转列表：{list(set1)}")
print(f"字典 转列表：{list(dict1)}")

# 转元组
print(f"列表 转元组：{tuple(list1)}")
print(f"元组 转元组：{tuple(tuple1)}")
print(f"字符串 转元组：{tuple(str1)}")
print(f"集合 转元组：{tuple(set1)}")
print(f"字典 转元组：{tuple(dict1)}")

# 转字符串
print(f"列表 转字符串：{str(list1)}")
print(f"元组 转字符串：{str(tuple1)}")
print(f"字符串 转字符串：{str(str1)}")
print(f"集合 转字符串：{str(set1)}")
print(f"字典 转字符串：{str(dict1)}")

# 转集合
print(f"列表 转集合：{set(list1)}")
print(f"元组 转集合：{set(tuple1)}")
print(f"字符串 转集合：{set(str1)}")
print(f"集合 转集合：{set(set1)}")
print(f"字典 转集合：{set(dict1)}")

# 没有键值对 无法转字典

# 4.容器排序 sorted(容器,reverse=True) 排序结果放在列表对象中
list1 = [71, 22, 63, 74, 15]
tuple1 = (71, 2, 533, 64, 15)
str1 = "Iven likes apple"
set1 = {12, 42, 37, 49, 15}
dict1 = {'Iven':99, 'rosenn':93, 'Starry':89}

print(f"列表 排序：{sorted(list1)}")
print(f"元组 排序：{sorted(tuple1)}")
print(f"字符串 排序：{sorted(str1)}")
print(f"集合 排序：{sorted(set1)}")
print(f"字典 排序：{sorted(dict1)}")

print(f"列表 反向排序：{sorted(list1, reverse=True)}")
print(f"元组 反向排序：{sorted(tuple1, reverse=True)}")
print(f"字符串 反向排序：{sorted(str1, reverse=True)}")
print(f"集合 反向排序：{sorted(set1, reverse=True)}")
print(f"字典 反向排序：{sorted(dict1, reverse=True)}")