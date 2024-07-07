# 有顺序
height = int(input("请输入您的身高(cm)："))
vip_level = int(input("请输入您的vip等级："))
day = int(input("请输入今天是几号："))
if height < 120:
    print("身高小于120cm，免费")
elif vip_level > 3:
    print("vip级别大于3，免费")
elif day == 1:
    print("今天是1号免费日，免费")
else:
    print("不好意思，您需额外购票10元")

# else可以省略不写，效果相当于3个同等的if
# 简化流程
if int(input("请输入您的身高(cm)：")) < 120:
    print("身高小于120cm，免费")
elif int(input("请输入您的vip等级：")) > 3:
    print("vip级别大于3，免费")
elif int(input("请输入今天是几号：")) == 1:
    print("今天是1号免费日，免费")
else:
    print("不好意思，您需额外购票10元")

# 练习
num = 10
if int(input("请输入第一次猜想的数字：")) == num:
    print("一次就猜对啦！")
elif int(input("sorry，猜错啦，再猜一次：")) == num:
    print("第二次就猜对啦！")
elif int(input("sorry，猜错啦，再猜一次：")) == num:
    print("还不错，第三次猜对啦！")
else:
    print("全部猜错，我想的是%d" % num)