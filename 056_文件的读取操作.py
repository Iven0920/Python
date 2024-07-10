# open(name, mode, encoding) 打开文件 mode 只读r、写入w、追加a
f = open("related_data/test.txt", "r", encoding="UTF-8")
print(type(f))

# read(num) num从文件中读取的数据长度(单位是字节) 不传入代表所有数据 返回字符串
# * 连续使用read读取 第二次read的部分会在第一次read结束位置接着读取 有读取指针
print(f"读取十个字节的结果：{f.read(10)}")
print(f"读取全部内容的结果：{f.read()}")

# readlines() 文件内容一次性读取，返回一个列表，每一行的数据为一个元素
f = open("related_data/test.txt", "r", encoding="UTF-8")
lines = f.readlines()
print(f"lines对象的类型：{type(lines)}，内容为{lines}")

# readline() 一次读取一行内容
f = open("related_data/test.txt", "r", encoding="UTF-8")
lines = f.readline()
print(f"第一行的类型：{type(lines)}，内容为{lines}")
lines = f.readline()
print(f"第二行的类型：{type(lines)}，内容为{lines}")
lines = f.readline()
print(f"第二行的类型：{type(lines)}，内容为{lines}")

# for循环读取
f = open("related_data/test.txt", "r", encoding="UTF-8")
for line in f:
    print(f"每一行的数据为：{line}")

# close()关闭文件 解除文件占用
f.close()
# import time 
# time.sleep(500000)

# with open 执行完相关语句自动关闭文件
with open("related_data/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行的数据为：{line}")
# import time 
# time.sleep(500000)

# 练习
# 第一种
count = 0
with open("related_data/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        count += line.count("Iven")
print(f"Iven出现的次数为:{count}")

# 第二种
count = 0
f = open("related_data/test.txt", "r", encoding="UTF-8")
test_str = f.read()
count += test_str.count("Iven")
print(f"Iven出现的次数为:{count}")
f.close()

# 第三种
count = 0
f = open("related_data/test.txt", "r", encoding="UTF-8")
test_list = f.readlines()
for element in test_list:
    count += element.count("Iven")
print(f"Iven出现的次数为:{count}")
f.close()

# 第四种
count = 0
f = open("related_data/test.txt", "r", encoding="UTF-8")
row = f.readline()
while row != "":
    count += row.count("Iven")
    row = f.readline()
print(f"Iven出现的次数为:{count}")
f.close()

# 第五种 有弊端 若无空格拆分不了
count = 0
f = open("related_data/test.txt", "r", encoding="UTF-8")
for line in f:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == "Iven":
            count += 1
print(f"Iven出现的次数为:{count}")
f.close()