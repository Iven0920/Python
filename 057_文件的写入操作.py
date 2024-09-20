import time

# 设置test_write.txt不存在 自动创建文件
f = open("related_data/test_write.txt", "w", encoding="UTF-8")
# write 积攒在程序的内存中，又称为缓冲区  
f.write("Hello World!")
# // time.sleep(5000000)

# flush 内容刷新 刷新后内容才会真正写入文件
f.flush()
# // time.sleep(5000000)
# close内置flush功能
f.close()

#  若存在 写入操作会清空原文件
f = open("related_data/test_write.txt", "w", encoding="UTF-8")
# write 积攒在程序的内存中，又称为缓冲区  
f.write("Iven")
f.close()