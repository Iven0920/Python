f_r = open("related_data/bill.txt", "r", encoding="UTF-8")
f_w = open("related_data/bill.txt.bak", "w", encoding="UTF-8")

line = f_r.readline()
while line != "":
    if line.count("测试") == 0:
        f_w.write(line)
    line = f_r.readline()
f_w.flush()
f_r.close()
f_w.close()

f_r = open("related_data/bill.txt", "r", encoding="UTF-8")
f_w = open("related_data/bill.txt.bak", "r", encoding="UTF-8")
print(f"原数据为：\n{f_r.read()}")
print(f"备份好的数据为：\n{f_w.read()}")
f_r.close()
f_w.close()