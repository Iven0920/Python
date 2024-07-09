# 元组 同列表一样但元素不可被修改
# // t0 = (1, 2, 3, 3 , 5, 6)
# // t0[0] = 4
# // print(t0)
# * 特例 元组里的list是可以修改的
t0 = ([1, 2, 3], 3 , 5, 6)
t0[0][2] = 4
print(t0)

# 空元组
# 变量名称 = ()
# 变量名称 = tuple()

t1 = (1, "Iven", True)
t2 = ()
t3 = tuple()
print(f"tuple1的类型是：{type(t1)}，内容为:{t1}")
print(f"tuple2的类型是：{type(t2)}，内容为:{t2}")
print(f"tuple3的类型是：{type(t3)}，内容为:{t3}")

# 定义单个元素的元组 注意逗号
t4 = ("Iven", )
str = ("Iven")
print(f"tuple4的类型是：{type(t4)}，内容为:{t4}")
print(f"str的类型是：{type(str)}，内容为:{str}")

# 元组的嵌套
t5 = ((1, 2, 3,), (2, 3, 4))
print(f"tuple5的类型是：{type(t5)}，内容为:{t5}")

# 通过下标索引取出内容
num = t5[1][2]
print(f"从嵌套元组取出了：{num}")

# 元组相关操作
# 1.index
t6 = ("Iven", "Python", "handsome")
index = t6.index("Python")
print(f"元素Python的索引为{index}")
# 2.count
t7 = (1, 2, 3, 4, 5, 4, 3, 2, 1)
num = t7.count(1)
print(f"元素1的个数为{num}")
# 3.len
t8 = (1, 2, 3, 4, 5, 4, 3, 2, 1)
num = len(t8)
print(f"元组8的元素个数为{num}")

# 元组遍历
# while
index = 0
while index < len(t8):
    print(f"元组的元素有：{t8[index]}")
    index += 1
# for
for element in t8:
    print(f"元组的元素有：{element}")

# 练习
t9 = ('Iven', 18, ['football', 'music'])
age_index = t9.index(18)
name = t9[0]
del t9[2][0]
t9[2].append('coding')
print(f"年龄的下标索引为：{age_index}")
print(f"学生姓名为：{name}")
print(f"删除和增加后元组元素：{t9}")