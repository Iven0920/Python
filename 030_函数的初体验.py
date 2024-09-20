# 统计字符串长度 不使用内置函数len()
str1 = "Coding"
str2 = "Iven"
str3 = "surfing"

count = 0
for i in str1:
    count += 1
print(f"字符串长度为{count}")

count = 0
for i in str2:
    count += 1
print(f"字符串长度为{count}")

count = 0
for i in str3:
    count += 1
print(f"字符串长度为{count}")

# 可以使用函数 已组织好的 可重复利用的 针对特定功能
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串长度为{count}")

my_len(str1)
my_len(str2)
my_len(str3)
