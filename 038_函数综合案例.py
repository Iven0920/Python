money = 5000000
name = input("请输入您的姓名：")

def find_money(find_bool):
    if find_bool == True:
        print("--------------------查询余额--------------------")
    print(f"{name}，您好，您的当前余额为：{money}")
    main_menu(name)

def save_money(num):
    print("--------------------存款--------------------")
    global money
    money += num
    print(f"{name}，您好，您已成功存款{num}元")
    find_money(False)
    main_menu(name)

def pick_money(num):
    print("--------------------取款--------------------")
    global money
    money -= num
    print(f"{name}，您好，您已成功取款{num}元")
    find_money(False)
    main_menu(name)

def main_menu(name):
    print("--------------------主菜单--------------------")
    print(f"{name}，您好，欢迎来到银行ATM。请选择操作：")
    # 一个\t对不齐 就要两个
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")

    choice = int(input("请输入您的选择："))
    if choice == 1:
        find_money(True)
    elif choice == 2:
        num = int(input("请输入您要存入的金钱数额："))
        save_money(num)
    elif choice == 3:
        num = int(input("请输入您要取出的金钱数额："))
        pick_money(num)
    else:
        exit()

main_menu(name)

# 另一种思路 
money = 5000000
name = input("请输入您的姓名：")

def find_money(find_bool):
    if find_bool == True:
        print("--------------------查询余额--------------------")
    print(f"{name}，您好，您的当前余额为：{money}")

def save_money(num):
    print("--------------------存款--------------------")
    global money
    money += num
    print(f"{name}，您好，您已成功存款{num}元")
    find_money(False)

def pick_money(num):
    print("--------------------取款--------------------")
    global money
    money -= num
    print(f"{name}，您好，您已成功取款{num}元")
    find_money(False)

def main_menu(name):
    print("--------------------主菜单--------------------")
    print(f"{name}，您好，欢迎来到银行ATM。请选择操作：")
    # 一个\t对不齐 就要两个
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")

while True:
    keyboard_input = main_menu(name)
    if keyboard_input == "1":
        find_money(True)
        continue
    elif keyboard_input == "2":
        num = int(input("请输入您要存入的金钱数额："))
        save_money(num)
        continue
    elif keyboard_input == "3":
        num = int(input("请输入您要取出的金钱数额："))
        pick_money(num)
        continue
    else:
        print("程序退出")
        break