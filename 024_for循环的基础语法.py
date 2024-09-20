name = "Iven"

# 临时变量x 待处理数据集name 理论上不可以无限循环
for x in name:
    print(x)

# 练习
name = "Iven enjoys the time of coding"
num = 0
for i in name:
    if i == "n":
        num += 1
print(f"{name}中一共出现了{num}个n")
