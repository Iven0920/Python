i = 0
while i < 100:
    print("Hello Iven")
    i += 1

# 练习1
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(f"从1到100的和为：{sum}")

# 练习2
import random
num = random.randint(1,100)
guess_result = False
final_guess_num = 0

while guess_result == False:
    final_guess_num += 1
    guess_num = int(input("请输入你猜想的数字(1-100):"))
    if guess_num == num:
        print("恭喜你，猜对啦！")
        guess_result = True
    elif guess_num > num:
        print("猜错啦，猜的有点大哦\n")
    else:
        print("猜错啦，猜的有点小哦\n")
print(f"您一共猜了{final_guess_num}次")

# 也可以是
while guess_result == False:
    final_guess_num += 1
    guess_num = int(input("请输入你猜想的数字(1-100):"))
    if guess_num == num:
        print("恭喜你，猜对啦！")
        guess_result = True
    else:
        if guess_num > num:
            print("猜错啦，猜的有点大哦\n")
        else:
            print("猜错啦，猜的有点小哦\n")
print(f"您一共猜了{final_guess_num}次")