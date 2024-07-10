my_str = "Iven enjoys surfing"
value = my_str[2]
print(f"取下标为2的元素是:{value}")
value = my_str[-17]
print(f"取下标为-17的元素是:{value}")

# 跟元组一样，字符串是一个无法修改的数据容器
# // my_str[2] = 'h'

# index
print(f"字符串中的enjoys的起始下标索引是{my_str.index('enjoys')}")

# replace(1, 2) 字符串替换  并不是修改字符串本身，而是得到了新的字符串，所以必须要重新定义 1被替换的 2替换的
new_str = my_str.replace('Iven', 'Rosennn')
print(f"源字符串还是：{my_str}")
print(f"新的字符串是：{new_str}")
my_str = my_str.replace('Iven', 'Rosennn')
print(f"也可以覆盖自己：{my_str}")

# split 字符串分割  字符串本身不变 得到了一个列表对象
# 按空格进行切分
split_str = my_str.split(" ")
print(f"字符串分割：{split_str}，类型为{type(split_str)}")

# strip 去除前后空格以及换行符 去除指定字符串strip("字符串")
my_str = "   Iven enjoys surfing   "
print(my_str.strip())
my_str = "12Iven enjoys surfing21"
# * 只对字符串的开头或结尾生效 若被去除的字符在中间 则不生效 可用replace
new_my_str = my_str.strip('n')
print("n不在两头：", new_my_str)
new_my_str = my_str.strip('12')
print("12在两头：", new_my_str)

# count 字符串中某字符串出现次数
print(f"n出现的次数是{my_str.count('n')}")

# len 字符串长度
print(f"字符串长度{len(my_str)}")

#  练习
lian_xi_str = "rosenn likes rose"
# 引号嵌套注意用不同的引号类型
print(f"字符串中共有{lian_xi_str.count('rose')}个rose")
lian_xi_str = lian_xi_str.replace(' ', '|')
print("替换后的字符串：", lian_xi_str)
lian_xi_str = lian_xi_str.split('|')
print(f'分割字符串后得到的列表为{lian_xi_str}' )