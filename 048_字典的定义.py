# 字典 key:value 键:值 不可以使用下标索引 不可以有两个相同key 后面的会覆盖前面的 
my_dict = {'Iven':99, 'rosenn':93, 'Starry':89}
my_dict_1 = {'Iven':99, 'Iven':66, 'rosenn':93, 'Starry':89}

# 空字典 变量名称 = {} 变量名称 = dict()
my_dict_2 = {}
my_dict_3 = dict()
print(f"字典1的内容：{my_dict}，类型为：{type(my_dict)}")
print(f"两个Iven key字典1的内容：{my_dict_1}")
print(f"字典2的内容：{my_dict_2}，类型为：{type(my_dict_2)}")
print(f"字典3的内容：{my_dict_3}，类型为：{type(my_dict_3)}")

# 取value
print(f"Iven的考试分数为：{my_dict['Iven']}")

# 字典嵌套 key（不可为字典）其他数据类型都可 value任意
qian_tao_dict = {
    'Iven':{
    '语文':99, 
    '数学':98, 
    '英语':97}, 
    'rosen':{
    '语文':94, 
    '数学':91, 
    '英语':84},
    'Starry':{
    '语文':79,
    '数学':94, 
    '英语':91}
    }
print(qian_tao_dict)
print(f"Iven的数学分数为:{qian_tao_dict['Iven']['数学']}")