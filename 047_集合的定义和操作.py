# 集合 自动去重 元素不可重复 顺序不确定无序  不支持下标索引{} 空集合 变量名称=set()
my_set = {'Iven', 'Python', 'work', 'happy', 'Iven', 'Python', 'work', 'happy'}
my_set_empty = set()
print(f'my_set的内容是{my_set}，类型是{type(my_set)}')
print(f'my_set_empty的内容是{my_set_empty}，类型是{type(my_set_empty)}')

# add 添加新元素
my_set.add('handsome')
my_set.add('Iven')
print(f'my_set添加内容后的内容是{my_set}，类型是{type(my_set)}')

# remove 移除元素
my_set.remove('happy')
print(f'my_set删除happy后的内容是{my_set}，类型是{type(my_set)}')

# pop 取出、删除元素 随机
element = my_set.pop()
print(f'my_set取出的元素是{element}，取出后集合为{my_set}')

# clear 清空集合
my_set.clear()
print(f'清空后集合为{my_set}')

# 1.difference(2) 取出集合1和集合2的差集 1有2没有 
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.difference(set2)
print(f'set1的内容是{set1}')
print(f'set2的内容是{set2}')
print(f'set3的内容是{set3}')

# 1.difference_update(2) 消除2个集合的差集 在1上删除和2一样的元素
set1 = {1, 2, 3}
set2 = {1, 4, 5}
print(f'set1的内容是{set1}')
print(f'set2的内容是{set2}')
set1.difference_update(set2)
print(f'更新后set1的内容是{set1}')

# 1.union(2) 合并新集合
set1 = {1, 2, 3}
set2 = {1, 4, 5}
print(f'set1的内容是{set1}')
print(f'set2的内容是{set2}')
set3 = set1.union(set2)
print(f'合并后set3的内容是{set3}')

# len 统计元素数量
set1 = {1, 2, 3}
print(f'set1的内容是{set1},数量是{len(set1)}')

# 遍历
# * 没有下标索引 不支持while
for element in set1:
    print(element)

# 练习
my_list = ['Iven', 'Python', 'work', 'student', '程序员', 'student', '程序员']
my_set = set()
for element in my_list:
    my_set.add(element)

print(f"有列表：{my_list}")
print(f"去重后的集合对象为：{my_set}")