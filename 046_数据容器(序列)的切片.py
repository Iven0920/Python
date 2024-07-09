# 序列：内容连续、有序。有下标索引，字符串、元组、列表
# 常用操作：切片 序列[起始下标:结束下标:步长]（不包含结束下标的元素） 步长为负数，起始和结束也应反向标记
# list
my_list = [0, 1, 2, 3, 4, 5, 6]
print(f"my_list切片为：{my_list[1:4]}")

# tuple
my_tuple = (0, 1, 2, 3, 4, 5, 6)
print(f"my_tuple切片为：{my_tuple[:]}")

# str
my_str = "0123456"
print(f"my_str切片为：{my_str[::2]}")

# 反向list
my_list = [0, 1, 2, 3, 4, 5, 6]
print(f"my_list切片为：{my_list[3:1:-1]}")

# 反向tuple
my_tuple = (0, 1, 2, 3, 4, 5, 6)
print(f"my_tuple切片为：{my_tuple[::-2]}")

# 反向str 序列翻转
my_str = "0123456"
print(f"my_str切片为：{my_str[::-1]}")

# 练习
lian_xi_str = '油加,nohtyP习学力努要,nevI'
str_piece = lian_xi_str[::-1]
str_split = str_piece.split(',')
result = str_split[1].replace('要努力学习', '')
print(f"字符串变换历程:\n{lian_xi_str}\n{str_piece}\n{str_split}\n{result}")