# for循环外部不建议输出内部变量 不规范
# //for i in range(5):
# //    print(i)
# // print(i)

# 规范
i = 0
for i in range(5):
    print(i)
print(i)