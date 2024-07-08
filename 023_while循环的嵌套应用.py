i = 1
while i <= 100:
    print(f"今天是第{i}天，准备表白......")

    j = 1
    while j <= 10:
        print(f"送给小美第{j}只玫瑰花")
        j += 1
    
    print("小美 我喜欢你！")
    i += 1
print(f"坚持到第{i - 1}天，表白成功！")

# 要注意循环条件的设置，避免无限循环

# * 补充知识 print输出不换行
print("Hello")
print("World")

print("Hello", end='')
print("World", end='')

# * 补充知识 制表符\t 当空格使用 并与下一行对应部分进行对齐
print("\n")
print("Hello World!")
print("Iven Starry")

print("Hello\tWorld!")
print("Iven\tStarry")

# 练习 99乘法表
row = 1

while row <= 9:
    i = 1
    while i <= row:
        print(f"{i}*{row}={i * row}\t", end='')
        i += 1
    # print空内容就是换行
    print()
    row += 1
