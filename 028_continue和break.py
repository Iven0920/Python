# continue 中断本次循环 进入下一次循环 用于while和for 只在所在循环执行下一次操作
for i in range(1, 6):
    print("Iven")
    continue
    print("Hello")

for i in range(1, 6):
    print("Iven")
    for j in range(1, 6):
        print("Hello")
        continue
        print("World!")
    print("Handsome")

# break 直接结束循环 用于while和for 只在所在循环结束
for i in range(1, 10):
    print("Iven")
    break
    print("Handsome")
print("Good")

for i in range(1, 5):
    print("Iven")
    for j in range(1, 5):
        print("Hello")
        break
        print("World")
    print("Handsome")
print("Good")