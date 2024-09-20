print("请告诉我你是谁？")
name = input()
print("我知道了，你是: %s" % name )

# 提示语直接写入input
name = input("请告诉我你是谁？\n")
print("我知道了，你是: %s" % name )

# input默认输入字符串 可用int转换
num = input("你的银行卡密码是：\n")
num = int(num)
print("你的银行卡密码是：" , type(num))

# 练习
user_name = input("您的姓名是：")
user_type = input("您的会员卡类型为：")
print("您好：", user_name, "，您是尊贵的：", user_type, "用户，欢迎您的光临")
print("您好：" + user_name + "，您是尊贵的：" +  user_type + "用户，欢迎您的光临")
print(f"您好：{user_name}，您是尊贵的：{user_type}用户，欢迎您的光临")
print("您好：%s，您是尊贵的：%s用户，欢迎您的光临" % (user_name, user_type))
# 不能直接输出还没输入的语句~
# // print(f"您好:{input("您的姓名是:")},您是尊贵的:{input("您的会员卡类型为:")}用户，欢迎您的光临")