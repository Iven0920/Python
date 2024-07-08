# for 待处理数据集 严格称之为序列类型 其内容可以一个个取出 包括 字符串 列表 元组

# range(num) 从0开始到num 不含num
for x in range(10):
    print(f"{x}\t", end='')
print()

# range(num1, num2) 从num1开始到num2 不含num2
for x in range(5, 10):
    print(f"{x}\t", end='')
print()

# range(num1, num2, step) 从num1开始到num 不含num2 步长为step
for x in range(5, 10, 2):
    print(f"{x}\t", end='')
print()

# 练习
num = 100
count = 0
for i in range(1, num):
    if i % 2 == 0:
        count += 1
print(f"从1到{num}（不包含{num}）共有{count}个偶数")