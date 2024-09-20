"""
函数定义时的x和y 形式参数 表示函数声明将要使用2个参数  
实际调用中 5和6为实际参数 函数执行时实际使用的参数值
"""

def add(x, y):
    z = x + y
    print(f"{x} + {y} 的计算结果是：{z}")

add(5, 6)

# 练习
def judge(age):
    print("您好，", end='')
    if age >= 18:
        print("您已成年，需要购票！")
    else:
        print("您未成年，无需购票！")
judge(int(input("欢迎来到游乐场，请输入您的年龄:")))