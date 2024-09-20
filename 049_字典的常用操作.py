# dict[key] = value 新增/更新元素
my_dict = {'Iven':99, 'rosenn':93, 'Starry':89}
my_dict['Bob'] = 95
print(f"新增后的字典为:{my_dict}")
my_dict['Bob'] = 90
print(f"更新后的字典为:{my_dict}")

# pop(key) 删除元素
score = my_dict.pop('Bob')
print(f"删除后的字典为:{my_dict}，他的成绩是{score}")

# clear 清空元素
my_dict.clear()
print(f"清空后的字典为:{my_dict}")

# dict.keys() 得到字典全部key
my_dict = {'Iven':99, 'rosenn':93, 'Starry':89}
keys = my_dict.keys()
print(f'字典中全部key值：{keys}')

# 遍历
# 下面二者效果完全相同 都是取key 不支持下标索引不能用while
for key in keys:
    print(f'字典的key是:{key}')
    print(f'对应的value是：{my_dict[key]}')

for key in my_dict:
    print(f'字典的key是:{key}')
    print(f'对应的value是：{my_dict[key]}')

# len 统计元素数量
print(f"元素数量：{len(my_dict)}")

# 练习
practice_dict = {
    'Iven':{
        '部门':'科技部',
        '工资':3000,
        '级别':1
    }, 
    'Rosen':{
        '部门':'市场部', 
        '工资':5000, 
        '级别':2
    },
    'Starry':{
    '部门':'市场部', 
    '工资':7000, 
    '级别':3
    },
    'Alen':{
    '部门':'科技部', 
    '工资':4000, 
    '级别':1},
    'Bob':{
    '部门':'市场部', 
    '工资':6000, 
    '级别':2
    }
    }
print(f'当前员工信息如下：\n{practice_dict}')
for name in practice_dict:
    if practice_dict[name]['级别'] == 1:
        practice_dict[name]['工资'] += 1000
        practice_dict[name]['级别'] += 1
print(f'所有级别为1的员工升职加薪后，员工信息如下：\n{practice_dict}')