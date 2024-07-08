import random
num = random.randint(1, 10)
guess_num = int(input("第一次尝试，输入你猜想的数字(1-10)"))

if guess_num == num:
    print("一次猜对啦")
else:
    print("猜错啦，猜的有点小")if(guess_num < num)else print("猜错啦，猜的有点大")
    if int(input("第二次尝试，输入你猜想的数字(1-10)")) == num:
        print("第二次就猜对啦！")
    else:
        print("猜错啦，猜的有点小")if(guess_num < num)else print("猜错啦，猜的有点大")
        if int(input("第二次尝试，输入你猜想的数字(1-10)")) == num:
            print("还不错，第三次猜对啦！")
        else:
            print("猜错啦，猜的有点小")if(guess_num < num)else print("猜错啦，猜的有点大")
            print("Game Over")
print("最终答案是：%d" % num)

# 也可以用 else(if...else..)嵌套