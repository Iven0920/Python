# 1.查询某元素的列表下标 列表.index(元素) index就是列表对象（变量）内置的方法（函数）
my_list = ['Iven', 'coding', 'python']
index = my_list.index('Iven')
print(f"Iven在列表的下标索引值为:{index}")

# 2.修改特定下标的元素值
my_list[0] = 'Ivennn'
print(f"列表被修改元素值后，结果为{my_list}")

# 3.插入元组 insert
my_list.insert(1, 'handsome')
print(f"列表插入元素后，结果为{my_list}")

# 4.追加元素 append extend
my_list.append("surfing")
print(f"列表追加元素后，结果为{my_list}")

my_list_new = ['good', 'perfect']
my_list.extend(my_list_new)
print(f"列表追加一个新的列表后，结果为{my_list}")

# 5.删除元素 del .pop() 
del my_list[1]
print(f"列表删除一个元素后，结果为{my_list}")

delete_element = my_list.pop(2)
print(f"列表删除一个元素后，结果为{my_list},删除的元素是{delete_element}")

# 6.删除某元素的第一个匹配项 remove()
my_list = [1, 2, 3, 2, 1]
my_list.remove(2)
print(my_list)

# 7.整个列表清空 clear()
my_list.clear()
print(my_list)

# 8.统计列表内某元素的数量 count()
my_list = [1, 2, 3, 2, 1]
count = my_list.count(2)
print(f"2的个数为：{count}")

# 9，统计列表的全部元素数量
my_list = [1, 2, 3, 2, 1]
count = len(my_list)
print(f"列表元素的个数为：{count}")

# 练习
age_list = [21, 25, 21, 23, 22, 20]
age_list.append(31)
age_list_extend = [29, 33, 30]
age_list.extend(age_list_extend)
element1 = age_list[0]
print("取出的第一个元素为：%d" % element1)
element2 = age_list[-1]
print("取出的最后一个元素为：%d" % element2)
index = age_list.index(31)
print("元素31的下标位置为：%d" % index)
print(f"最终列表为：{age_list}")