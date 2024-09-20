# 提前定义i 注意规范
i = 0

for i in range(1, 101):
    print(f"今天是表白的第{i}天，加油坚持")
    for j in range (1, 11):
        print(f"给小美送的第{j}朵玫瑰花")
print(f"第{i}天，表白成功！")

# 练习
for row in range(1,10):
    for i in range(1, row+1):
        print(f"{i}*{row}={i*row}\t",end='')
    print()