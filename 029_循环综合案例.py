# 发工资
import random

total_money = 10000

for i in range(1, 21):
    num = random.randint(1, 11)
    if num < 5:
        print(f"员工{i}，绩效分{num}，低于5，不发工资，下一位")
        continue
    else:
        total_money -=1000
        print(f"向员工{i}发放工资1000元，公司账户剩余{total_money}")
    if total_money <= 0:
        print("没钱啦，下个月再发")
        break

# 优化
total_money = 10000
for i in range(1, 21):
    num = random.randint(1, 11)
    if num < 5:
        print(f"员工{i}，绩效分{num}，低于5，不发工资，下一位")
        continue
    if total_money >= 1000:
        total_money -= 1000
        print(f"向员工{i}发放工资1000元，公司账户剩余{total_money}")
    else:
        print(f"余额不足，公司账户剩余{total_money}，不足以发工资，不发了，下个月再来")
        break