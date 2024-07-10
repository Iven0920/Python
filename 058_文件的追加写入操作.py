# 设置test_append.txt不存在 自动创建文件
f = open("related_data/test_append.txt", "a", encoding="UTF-8")
# write 积攒在程序的内存中，又称为缓冲区  
f.write("Hello World!")
f.flush()
f.close()

# 已有append文件
# 设置test_append.txt不存在 自动创建文件
f = open("related_data/test_append.txt", "a", encoding="UTF-8")
# write 积攒在程序的内存中，又称为缓冲区  
f.write("\nIven!")
f.flush()
f.close()