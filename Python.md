# Python
github：https://github.com/IvenStarry  

学习视频网站：B站黑马程序员
https://www.bilibili.com/video/BV1qW4y1a7fU?p=1&vd_source=6fd71d34326a08965fdb07842b0124a7
## 第一章
### 第一个python程序
```python
print("Hello World!")
print("你好世界！")
```
## 第二章
### 字面量
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407061822489.png)
```python
# 整数
666
# 浮点数
13.14
# 字符串
"努力码代码的Iven"

print(666)
print(13.14)
print("努力码代码的Iven")
```

### 注释
```python
# 单行注释
print("Hello World!")

# 多行注释 “”“ 注释 ”“”
"""
这里可以写很多注释
hello~
"""
```
### 变量
```python
# 定义变量
money = 50
# print 输出变量内容
print("钱包还有", money)
# 买一个冰激凌花了10块
money = money - 10
print("买了冰激凌花费10元，还剩余", money, "元")
# 假设 每隔一小时 输出一下钱包的余量
print("现在是下午1点，钱包余额：", money)
print("现在是下午2点，钱包余额：", money)
print("现在是下午3点，钱包余额：", money)
print("现在是下午4点，钱包余额：", money)
print("现在是下午5点，钱包余额：", money)
print("现在是下午6点，钱包余额：", money)

# 练习 求钱包余额
money = 50
print("当前钱包余额：", money)
money = money - 10
print("购买了冰激凌花费10元，当前钱包余额：", money)
money = money - 5
print("购买了可乐花费5元，当前钱包余额：", money)
```

### 数据类型
```python
# type()查看数据类型
print(type("iven码代码"))
print(type(666))
print(type(11.123))

int_type = type(888)
print(int_type)

name = "Iven码代码"
name_type = type(name)
print(name_type)

# * 变量没有类型 里面存储的数据有类型
```

### 数据类型转换
```python
"""
int(x)
float(x)
str(x) 
"""

num_str = str(11)
print(type(num_str), num_str)

# 字符串转数字 字符串的内容必须是数字
# // print(int("Iven"))

# 浮点转整数 丢失精度
int_num = int(11.345)
print(type(int_num), int_num)

# 整数转浮点
float_num = float(11)
print(type(float_num), float_num)
```

### 标识符
```python
# Rule 1: 内容限定 中 英 数 下划线_
# 中文不推荐使用 
# ! 数字不可以在开头
# // 1_name = "张三"
# // name_! = "Iven"
name_ = "Iven"
_name = "Iven"
name_1 = "Iven"

# Rule 2:大小写敏感
Name = "Iven"
name = "iven"
print(Name)
print(name)

# Rule 3:不可使用关键字 改大小写可以
# // class = 1
# //def = 1
Class = 1

# 命名规范 全小写 下划线分离单词 见明知意
```

### 运算符
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407071112090.png)
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407071131782.png)
```python
print("1 + 1 = ", 1 + 1)
print("2 - 1 = ", 2 - 1)
print("3 * 3 = ", 3 * 3)
print("4 / 2 = ", 4 / 2)
print("11 // 2 = ", 11 // 2)
print("9 % 2 = ", 9 % 2)
print("2 ** 2 = ", 2 ** 2)

# 赋值运算符
num = 1 + 2 * 3
# 复合赋值运算符
num = 1
num += 1
print("num += 1", num)
num -= 1
print("num -= 1", num)
num *= 4
print("num *= 4", num)
num /= 2
print("num /= 2", num)
num = 3
num %= 2
print("num %= 2", num)
num **= 2
print("num **= 2", num)
num = 9
num //= 2
print("num //= 2", num)
```

### 字符串三种定义方式
```python
# 单引号定义法
name = 'Iven'
print(type(name))
# 双引号定义法
name = "Iven"
print(type(name))
# 三引号定义法
name = """
My
name
is
Iven
"""
print(type(name))

# 字符串里包含双引号
name = '"Iven"'
print(name)
# 字符串里包含单引号
name = "'Iven'"
print(name)
# 转义字符 \ 的使用
name = "\"Iven\""
print(name)
name = '\'Iven\''
print(name)
```

### 字符串拼接
```python
# 字符串字面量之间的拼接
print("努力码代码的" + "Iven")
# 字符串字面量和字符串变量的拼接
name = "Iven"
address = "Home"
tel = 123456
# * 字符串无法通过+连接非字符串拼接
# // print("我是：" + name + ", 我的地址是" + address +"，我的号码是："  + tel)
# 但可以用逗号隔开
print("我是：" + name + ", 我的地址是" + address +"，我的号码是："  , tel)
```

### 字符串格式化
```python
class_num = 60
avg_salary = 1244
message = "一个班一共%s人，一个年级有%s名同学" % (class_num, avg_salary)
print(message)

name = "Iven"
message = "我是%s" % name
print(message)

"""
占位符
%s 将内容转换成字符串
# %d 将内容转换成整数
# %f 将内容转换成浮点型
"""

name = "Iven"
age = 21
gpa = 3.59
print("我的名字是:%s ,我的年龄为：%d岁, 我的GPA为:%f" % (name, age, gpa))
```

### 字符串格式化的精度控制
```python

# todo 地方 m.n m控制宽度，设置宽度小于数字自身宽度不生效 n控制小数点精度，四舍五入
# e.g %5d 数字11  变为空格空格空格11，用三个空格补足宽度
# e.g %7.2f 数字11.255  先补足宽度 再四舍五入 空格空格11.26

num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果为：%5d" % num1)
print("数字11宽度限制1，结果为：%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果为：%7.2f" % num2)
print("数字11.345宽度不限制，小数精度2，结果为：%.2f" % num2)
```

### 字符串格式化的方式2
```python

# todo f"内容{变量}" 快速格式化 不做精度控制 原本输出 f:format
name = "Iven"
age = 21
gpa = 3.99
print(f"我叫{name}, 我的年龄是{age}, 我的GPA为{gpa}")
```

### 对表达式进行格式化
```python
# 表达式：一条具有明确执行结果的代码语句 1+1 2*2
print("1 * 1的结果是:%d" % (1 * 1))
print(f"1 * 1的结果是:{1 * 1}")
print("字符串在Python的类型名是: %s" % type("字符串"))

# 小练习
name = "努力码代码的Iven"
stock_price = 19.99
stock_code = 1234567
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司:{name},股票代码:{stock_price},当前股价:{stock_price}")
print("每日增长系数:%.1f. 经过%d天的增长后, 股价达到了: %.2f" % (stock_price_daily_growth_factor, growth_days, stock_price * stock_price_daily_growth_factor **growth_days))
```

### 数据输入(input语句)
```python
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
```

## 第三章
### 布尔类型和比较运算符
```python
# Bool True False
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}，类型为{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}，类型为{type(bool_2)}")
result = 10 > 5
print(f"10 > 5 的结果为：{result}，数据类型为：{type(result)}")
print(f"10 > 5 的结果为：{10 > 5}，数据类型为：{type(10 > 5)}")

str_1 = "Iven"
str_2 = "iven"
print(f"Iven 和 iven 的比较结果为{str_1 == str_2}")
```

### if语句的基本格式
```python
age = 30

if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")
print("时间过的真快呀")

# 练习
print("欢迎来到儿童游乐园，儿童免费，成年收费")
age = int(input("输入您的年龄:"))
if age >= 18:
    print("您已成年，游玩应补票10元")
print("祝您游玩愉快！")
```

### if else组合判断
```python
age = int(input("请输入你的年龄："))

if age >= 18:
    print("您已成年, 需要买票10元")
else:
    print("您未成年, 可以免费游玩")

# 练习
height = int(input("请输入您的身高(cm)："))
if height >= 120:
    print("您的身高超过120cm，游玩需要购票10元")
else:
    print("您的身高未超过120cm，可以免费游玩")
print("祝您游玩愉快！")

```

### if elif else组合使用的语法
```python
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
```

### 判断语句的嵌套
```python
if int(input("输入您的身高：")) > 120:
    print("身高超出限制，不可免费")
    print("但是，如果vip级别大于3，可以免费")
    if int(input("请输入您的vip级别：")) > 3:
        print("恭喜您 ，vip级别达标，可以免费")
    else:
        print("sorry 需要买票~")
else:
    print("欢迎小朋友，免费游玩~")

age = 20
year = 3
level = 3
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if year > 2:
            print("恭喜您，年龄和入职时间都达标，可以领取礼物")
        elif level > 3:
            print(" 恭喜您，年龄和级别达标，可以领取礼物")
        else:
            print("不好意思，尽管年龄达标，但入职时间和级别都不达标")
    else:
        print("不好意思，年龄太大了，不可以领取礼物")
else:
    print("不好意思，小朋友不可以领取")
```

### 判断语句的综合案例
```python
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
```

## 第四章
### while循环的基础应用
```python
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
```

### while循环的嵌套应用
```python
i = 1
while i <= 100:
    print(f"今天是第{i}天，准备表白......")

    j = 1
    while j <= 10:
        print(f"送给小美第{j}只玫瑰花")
        j += 1
    
    print("小美 我喜欢你！")
    i += 1
print(f"坚持到第{i - 1}天，表白成功！")

# 要注意循环条件的设置，避免无限循环

# * 补充知识 print输出不换行
print("Hello")
print("World")

print("Hello", end='')
print("World", end='')

# * 补充知识 制表符\t 当空格使用 并与下一行对应部分进行对齐
print("\n")
print("Hello World!")
print("Iven Starry")

print("Hello\tWorld!")
print("Iven\tStarry")

# 练习 99乘法表
row = 1

while row <= 9:
    i = 1
    while i <= row:
        print(f"{i}*{row}={i * row}\t", end='')
        i += 1
    # print空内容就是换行
    print()
    row += 1

```

### for循环的基础语法
```python
name = "Iven"

# 临时变量x 待处理数据集name 理论上不可以无限循环
for x in name:
    print(x)

# 练习
name = "Iven enjoys the time of coding"
num = 0
for i in name:
    if i == "n":
        num += 1
print(f"{name}中一共出现了{num}个n")
```

### range语句
```python
# for 待处理数据集 严格称之为序列类型 其内容可以一个个取出 包括 字符串 列表 元组

# range(num) 从0开始到num 不含num
for x in range(10):
    print(f"{x}\t", end='')
print()

# range(num1, num2) 从num1开始到num2 不含num2
for x in range(5, 10):
    print(f"{x}\t", end='')
print()

# range(num1, num2, step) 从num1开始到num 不含num2 步长为step
for x in range(5, 10, 2):
    print(f"{x}\t", end='')
print()

# 练习
num = 100
count = 0
for i in range(1, num):
    if i % 2 == 0:
        count += 1
print(f"从1到{num}（不包含{num}）共有{count}个偶数")
```

### for循环的临时变量作用域
```python
# for循环外部不建议输出内部变量 不规范
# //for i in range(5):
# //    print(i)
# // print(i)

# 规范
i = 0
for i in range(5):
    print(i)
print(i)
```

### for循环的嵌套使用
```python
# 提前定义i 注意规范
i = 0

for i in range(1, 101):
    print(f"今天是表白的第{i}天，加油坚持")
    for j in range (1, 11):
        print(f"给小美送的第{j}朵玫瑰花")
print(f"第{i}天，表白成功！")

# 练习
for row in range(1,10):
    for i in range(1, row+1):
        print(f"{i}*{row}={i*row}\t",end='')
    print()
```

### continue和break
```python
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
```

### 循环综合案例
```python
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
```

## 第五章
### 函数的初体验
```python
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

```

### 函数的基础定义语法
```python
# def 函数名(传入参数): 函数体 return ()必须要有

def say_hi():
    print("Hi 我是Iven")

# 调用
say_hi()

# 练习
def flag():
    print("从0开始学Python")
    print("Iven加油！")
flag()
```

### 函数的传入参数
```python
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
```

### 函数的返回值定义语法
```python
def add(x, y):
    result = x + y
    return result
    print("这里不输出了")

r = add(5, 6)
```

### 函数返回值之None类型
```python
# 无返回值的函数 返回None这个字面量
def say_hi():
    print("Hi")

result = say_hi()
print(f"无返回值函数，输出的值是{result}，输出值的类型为{type(result)}")

# 主动返回
def say_hi():
    print("Hi")
    return None
result = say_hi()
print(f"无返回值函数，输出的值是{result}，输出值的类型为{type(result)}")

# 在if判断中，None等同于False
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None
result = check_age(16)
# * 只有True才进入if
if not result:
    print("未成年不可以进入")

# None用于声明无初始内容的变量
name = None
```

### 函数说明文档
```python
def add(x, y):
    """
    函数说明add函数可以接收3个参数，进行2数相加的功能
    :param x: 形参x表示相加的一个数字
    :param y: 形参y表示相加的另一个数字
    :return: 返回值是2数相加的结果
    """
    result = x + y
    print(f"2数相加的结果是{result}")
    return result

add(5, 6)
```

### 函数的嵌套调用
```python
def func_b():
    print("---2---")
def func_a():
    print("---1---")
    func_b()
    print("---3---")

func_a()
```

### 变量在函数中的作用域
```python
# 变量作用域即变量作用范围 局部变量（在函数体内部临时保存数据 当函数调用完成后 销毁局部变量）和全局变量
def test_a():
    num = 100
    print(num)
test_a()
# 出了函数体 局部变量无法使用
# // print(num)

# 全局变量
num = 100
def test_a():
    print(num)
test_a()
def test_b():
    print(num)
test_b()

# 在函数内修改全局变量
num = 100
def test_a():
    print(num)
test_a()
def test_b():
    num = 200 # 局部变量
    print(num)
test_b()
print(num) # 外面的不修改

# global关键字 在函数内部声明变量为全局变量
num = 100
def test_a():
    print(num)
test_a()
def test_b():
    global num
    num = 200 # 全局变量
    print(num)
test_b()
print(num) # 外面也修改了
```

### 函数综合案例
```python
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
```

## 第六章
### 数据容器入门
```python
# 一种可以容纳多份数据的Python数据类型
# 五类：列表 元组 字符串 集合 字典
```

### 列表的定义语法
```python
name_list = ['Iven', 'coding', 'python']
print(name_list)
print(type(name_list))

# * 十进制数字开头不允许为0   0o八进制 0b二进制 0x16进制
my_list = ['Iven', 920, True]
print(my_list)
print(type(my_list))

num_list = [[1, 2, 3], [4, 5, 6]]
print(num_list)
print(type(num_list))

# 定义空列表
# 变量名称 = []
# 变量名称 = list()
```

### 列表的下标索引
```python
my_list = ['Iven', "coding", "python"]
# 正向索引 0 1 2 
print(my_list[0])
print(my_list[1])
print(my_list[2])
# * 反向索引 -3 -2 -1
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

num_list = [[1, 2, 3], [4, 5, 6]]
print(num_list[1][1])
```

### 列表的常用操作方法
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407082313022.png)
```python
# 1.查询某元素的列表下标 列表.index(元素) index就是列表对象（变量）内置的方法（函数）
my_list = ['Iven', 'coding', 'python']
index = my_list.index('Iven')
print(f"Iven在列表的下标索引值为:{index}")

# 2.修改特定下标的元素值
my_list[0] = 'Ivennn'
print(f"列表被修改元素值后，结果为{my_list}")

# 3.插入元组 insert
my_list.insert(1, 'handsome')
print(f"列表插入元素后，结果为{my_list}")

# 4.追加元素 append extend
my_list.append("surfing")
print(f"列表追加元素后，结果为{my_list}")

my_list_new = ['good', 'perfect']
my_list.extend(my_list_new)
print(f"列表追加一个新的列表后，结果为{my_list}")

# 5.删除元素 del .pop() 
del my_list[1]
print(f"列表删除一个元素后，结果为{my_list}")

delete_element = my_list.pop(2)
print(f"列表删除一个元素后，结果为{my_list},删除的元素是{delete_element}")

# 6.删除某元素的第一个匹配项 remove()
my_list = [1, 2, 3, 2, 1]
my_list.remove(2)
print(my_list)

# 7.整个列表清空 clear()
my_list.clear()
print(my_list)

# 8.统计列表内某元素的数量 count()
my_list = [1, 2, 3, 2, 1]
count = my_list.count(2)
print(f"2的个数为：{count}")

# 9，统计列表的全部元素数量
my_list = [1, 2, 3, 2, 1]
count = len(my_list)
print(f"列表元素的个数为：{count}")

# 练习
age_list = [21, 25, 21, 23, 22, 20]
age_list.append(31)
age_list_extend = [29, 33, 30]
age_list.extend(age_list_extend)
element1 = age_list[0]
print("取出的第一个元素为：%d" % element1)
element2 = age_list[-1]
print("取出的最后一个元素为：%d" % element2)
index = age_list.index(31)
print("元素31的下标位置为：%d" % index)
print(f"最终列表为：{age_list}")
```

### 列表的循环遍历
```python
list = [1, 2, 3, 4, 5]
def list_while():
    index = 0
    while index < len(list):
        print(f"取出{list[index]}")
        index += 1
list_while()

def list_for():
    for index in range(len(list)):
        print(f"取出{list[index]}")
    for element in list:
        print(f"取出{element}")
list_for()

# 练习
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
new_list = []
count = 0
while count < len(num_list):
    if num_list[count] % 2 ==0:
        new_list.append(num_list[count])
    count += 1
print(f"新的列表对象中的元素有{new_list}")

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
new_list = []
count = 0
for element in num_list:
    if element % 2 ==0:
        new_list.append(element)
print(f"新的列表对象中的元素有{new_list}")
```
### 元组的定义和操作
```python
# 元组 同列表一样但元素不可被修改
# // t0 = (1, 2, 3, 3 , 5, 6)
# // t0[0] = 4
# // print(t0)
# * 特例 元组里的list是可以修改的
t0 = ([1, 2, 3], 3 , 5, 6)
t0[0][2] = 4
print(t0)

# 空元组
# 变量名称 = ()
# 变量名称 = tuple()

t1 = (1, "Iven", True)
t2 = ()
t3 = tuple()
print(f"tuple1的类型是：{type(t1)}，内容为:{t1}")
print(f"tuple2的类型是：{type(t2)}，内容为:{t2}")
print(f"tuple3的类型是：{type(t3)}，内容为:{t3}")

# 定义单个元素的元组 注意逗号
t4 = ("Iven", )
str = ("Iven")
print(f"tuple4的类型是：{type(t4)}，内容为:{t4}")
print(f"str的类型是：{type(str)}，内容为:{str}")

# 元组的嵌套
t5 = ((1, 2, 3,), (2, 3, 4))
print(f"tuple5的类型是：{type(t5)}，内容为:{t5}")

# 通过下标索引取出内容
num = t5[1][2]
print(f"从嵌套元组取出了：{num}")

# 元组相关操作
# 1.index
t6 = ("Iven", "Python", "handsome")
index = t6.index("Python")
print(f"元素Python的索引为{index}")
# 2.count
t7 = (1, 2, 3, 4, 5, 4, 3, 2, 1)
num = t7.count(1)
print(f"元素1的个数为{num}")
# 3.len
t8 = (1, 2, 3, 4, 5, 4, 3, 2, 1)
num = len(t8)
print(f"元组8的元素个数为{num}")

# 元组遍历
# while
index = 0
while index < len(t8):
    print(f"元组的元素有：{t8[index]}")
    index += 1
# for
for element in t8:
    print(f"元组的元素有：{element}")

# 练习
t9 = ('Iven', 18, ['football', 'music'])
age_index = t9.index(18)
name = t9[0]
del t9[2][0]
t9[2].append('coding')
print(f"年龄的下标索引为：{age_index}")
print(f"学生姓名为：{name}")
print(f"删除和增加后元组元素：{t9}")
```

### 字符串的定义和操作
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407091144825.png)
```python
my_str = "Iven enjoys surfing"
value = my_str[2]
print(f"取下标为2的元素是:{value}")
value = my_str[-17]
print(f"取下标为-17的元素是:{value}")

# 跟元组一样，字符串是一个无法修改的数据容器
# // my_str[2] = 'h'

# index
print(f"字符串中的enjoys的起始下标索引是{my_str.index('enjoys')}")

# replace(1, 2) 字符串替换  并不是修改字符串本身，而是得到了新的字符串，所以必须要重新定义 1被替换的 2替换的
new_str = my_str.replace('Iven', 'Rosennn')
print(f"源字符串还是：{my_str}")
print(f"新的字符串是：{new_str}")
my_str = my_str.replace('Iven', 'Rosennn')
print(f"也可以覆盖自己：{my_str}")

# split 字符串分割  字符串本身不变 得到了一个列表对象
# 按空格进行切分
split_str = my_str.split(" ")
print(f"字符串分割：{split_str}，类型为{type(split_str)}")

# strip 去除前后空格以及换行符 去除指定字符串strip("字符串")
my_str = "   Iven enjoys surfing   "
print(my_str.strip())
my_str = "12Iven enjoys surfing21"
# * 只对字符串的开头或结尾生效 若被去除的字符在中间 则不生效 可用replace
new_my_str = my_str.strip('n')
print("n不在两头：", new_my_str)
new_my_str = my_str.strip('12')
print("12在两头：", new_my_str)

# count 字符串中某字符串出现次数
print(f"n出现的次数是{my_str.count('n')}")

# len 字符串长度
print(f"字符串长度{len(my_str)}")

#  练习
lian_xi_str = "rosenn likes rose"
# 引号嵌套注意用不同的引号类型
print(f"字符串中共有{lian_xi_str.count('rose')}个rose")
lian_xi_str = lian_xi_str.replace(' ', '|')
print("替换后的字符串：", lian_xi_str)
lian_xi_str = lian_xi_str.split('|')
print(f'分割字符串后得到的列表为{lian_xi_str}' )
```

### 数据容器(序列)的切片
```python
# 序列：内容连续、有序。有下标索引，字符串、元组、列表
# 常用操作：切片 序列[起始下标:结束下标:步长]（不包含结束下标的元素） 步长为负数，起始和结束也应反向标记
# list
my_list = [0, 1, 2, 3, 4, 5, 6]
print(f"my_list切片为：{my_list[1:4]}")

# tuple
my_tuple = (0, 1, 2, 3, 4, 5, 6)
print(f"my_tuple切片为：{my_tuple[:]}")

# str
my_str = "0123456"
print(f"my_str切片为：{my_str[::2]}")

# 反向list
my_list = [0, 1, 2, 3, 4, 5, 6]
print(f"my_list切片为：{my_list[3:1:-1]}")

# 反向tuple
my_tuple = (0, 1, 2, 3, 4, 5, 6)
print(f"my_tuple切片为：{my_tuple[::-2]}")

# 反向str 序列翻转
my_str = "0123456"
print(f"my_str切片为：{my_str[::-1]}")

# 练习
lian_xi_str = '油加,nohtyP习学力努要,nevI'
str_piece = lian_xi_str[::-1]
str_split = str_piece.split(',')
result = str_split[1].replace('要努力学习', '')
print(f"字符串变换历程:\n{lian_xi_str}\n{str_piece}\n{str_split}\n{result}")
```

### 集合的定义和操作
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407092245561.png)
```python
# 集合 自动去重 元素不可重复 顺序不确定无序  不支持下标索引{} 空集合 变量名称=set()
my_set = {'Iven', 'Python', 'work', 'happy', 'Iven', 'Python', 'work', 'happy'}
my_set_empty = set()
print(f'my_set的内容是{my_set}，类型是{type(my_set)}')
print(f'my_set_empty的内容是{my_set_empty}，类型是{type(my_set_empty)}')

# add 添加新元素
my_set.add('handsome')
my_set.add('Iven')
print(f'my_set添加内容后的内容是{my_set}，类型是{type(my_set)}')

# remove 移除元素
my_set.remove('happy')
print(f'my_set删除happy后的内容是{my_set}，类型是{type(my_set)}')

# pop 取出、删除元素 随机
element = my_set.pop()
print(f'my_set取出的元素是{element}，取出后集合为{my_set}')

# clear 清空集合
my_set.clear()
print(f'清空后集合为{my_set}')

# 1.difference(2) 取出集合1和集合2的差集 1有2没有 
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.difference(set2)
print(f'set1的内容是{set1}')
print(f'set2的内容是{set2}')
print(f'set3的内容是{set3}')

# 1.difference_update(2) 消除2个集合的差集 在1上删除和2一样的元素
set1 = {1, 2, 3}
set2 = {1, 4, 5}
print(f'set1的内容是{set1}')
print(f'set2的内容是{set2}')
set1.difference_update(set2)
print(f'更新后set1的内容是{set1}')

# 1.union(2) 合并新集合
set1 = {1, 2, 3}
set2 = {1, 4, 5}
print(f'set1的内容是{set1}')
print(f'set2的内容是{set2}')
set3 = set1.union(set2)
print(f'合并后set3的内容是{set3}')

# len 统计元素数量
set1 = {1, 2, 3}
print(f'set1的内容是{set1},数量是{len(set1)}')

# 遍历
# * 没有下标索引 不支持while
for element in set1:
    print(element)

# 练习
my_list = ['Iven', 'Python', 'work', 'student', '程序员', 'student', '程序员']
my_set = set()
for element in my_list:
    my_set.add(element)

print(f"有列表：{my_list}")
print(f"去重后的集合对象为：{my_set}")
```

### 字典的定义
```python
# 字典 key:value 键:值 不可以使用下标索引 不可以有两个相同key 后面的会覆盖前面的 
my_dict = {'Iven':99, 'rosenn':93, 'Starry':89}
my_dict_1 = {'Iven':99, 'Iven':66, 'rosenn':93, 'Starry':89}

# 空字典 变量名称 = {} 变量名称 = dict()
my_dict_2 = {}
my_dict_3 = dict()
print(f"字典1的内容：{my_dict}，类型为：{type(my_dict)}")
print(f"两个Iven key字典1的内容：{my_dict_1}")
print(f"字典2的内容：{my_dict_2}，类型为：{type(my_dict_2)}")
print(f"字典3的内容：{my_dict_3}，类型为：{type(my_dict_3)}")

# 取value
print(f"Iven的考试分数为：{my_dict['Iven']}")

# 字典嵌套 key（不可为字典）其他数据类型都可 value任意
qian_tao_dict = {
    'Iven':{
    '语文':99, 
    '数学':98, 
    '英语':97}, 
    'rosen':{
    '语文':94, 
    '数学':91, 
    '英语':84},
    'Starry':{
    '语文':79,
    '数学':94, 
    '英语':91}
    }
print(qian_tao_dict)
print(f"Iven的数学分数为:{qian_tao_dict['Iven']['数学']}")
```
### 字典的常用操作
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407092333415.png)
```python
# dict[key] = value 新增/更新元素
my_dict = {'Iven':99, 'rosenn':93, 'Starry':89}
my_dict['Bob'] = 95
print(f"新增后的字典为:{my_dict}")
my_dict['Bob'] = 90
print(f"更新后的字典为:{my_dict}")

# pop(key) 删除元素
score = my_dict.pop('Bob')
print(f"删除后的字典为:{my_dict}，他的成绩是{score}")

# clear 清空元素
my_dict.clear()
print(f"清空后的字典为:{my_dict}")

# dict.keys() 得到字典全部key
my_dict = {'Iven':99, 'rosenn':93, 'Starry':89}
keys = my_dict.keys()
print(f'字典中全部key值：{keys}')

# 遍历
# 下面二者效果完全相同 都是取key 不支持下标索引不能用while
for key in keys:
    print(f'字典的key是:{key}')
    print(f'对应的value是：{my_dict[key]}')

for key in my_dict:
    print(f'字典的key是:{key}')
    print(f'对应的value是：{my_dict[key]}')

# len 统计元素数量
print(f"元素数量：{len(my_dict)}")

# 练习
practice_dict = {
    'Iven':{
        '部门':'科技部',
        '工资':3000,
        '级别':1
    }, 
    'Rosen':{
        '部门':'市场部', 
        '工资':5000, 
        '级别':2
    },
    'Starry':{
    '部门':'市场部', 
    '工资':7000, 
    '级别':3
    },
    'Alen':{
    '部门':'科技部', 
    '工资':4000, 
    '级别':1},
    'Bob':{
    '部门':'市场部', 
    '工资':6000, 
    '级别':2
    }
    }
print(f'当前员工信息如下：\n{practice_dict}')
for name in practice_dict:
    if practice_dict[name]['级别'] == 1:
        practice_dict[name]['工资'] += 1000
        practice_dict[name]['级别'] += 1
print(f'所有级别为1的员工升职加薪后，员工信息如下：\n{practice_dict}')
```
### 五类数据容器的对比
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407092345579.png)
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407092346918.png)

### 数据容器的通用操作
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407100012775.png)
```python
# 1.遍历 for while

# 2.统计
list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)
str1 = "Iven likes apple"
set1 = {1, 2, 3, 4, 5}
dict1 = {'Iven':99, 'rosenn':93, 'Starry':89}
# len 元素个数
print(f"列表 元素个数：{len(list1)}")
print(f"元组 元素个数：{len(tuple1)}")
print(f"字符串 元素个数：{len(str1)}")
print(f"集合 元素个数：{len(set1)}")
print(f"字典 元素个数：{len(dict1)}")

# max 最大元素
print(f"列表 最大元素：{max(list1)}")
print(f"元组 最大元素：{max(tuple1)}")
print(f"字符串 最大元素：{max(str1)}")
print(f"集合 最大元素：{max(set1)}")
print(f"字典 最大元素：{max(dict1)}")

# min 最小元素
print(f"列表 最小元素：{min(list1)}")
print(f"元组 最小元素：{min(tuple1)}")
print(f"字符串 最小元素：{min(str1)}")
print(f"集合 最小元素：{min(set1)}")
print(f"字典 最小元素：{min(dict1)}")

# 3.容器转换功能 
# 转列表
print(f"列表 转列表：{list(list1)}")
print(f"元组 转列表：{list(tuple1)}")
print(f"字符串 转列表：{list(str1)}")
print(f"集合 转列表：{list(set1)}")
print(f"字典 转列表：{list(dict1)}")

# 转元组
print(f"列表 转元组：{tuple(list1)}")
print(f"元组 转元组：{tuple(tuple1)}")
print(f"字符串 转元组：{tuple(str1)}")
print(f"集合 转元组：{tuple(set1)}")
print(f"字典 转元组：{tuple(dict1)}")

# 转字符串
print(f"列表 转字符串：{str(list1)}")
print(f"元组 转字符串：{str(tuple1)}")
print(f"字符串 转字符串：{str(str1)}")
print(f"集合 转字符串：{str(set1)}")
print(f"字典 转字符串：{str(dict1)}")

# 转集合
print(f"列表 转集合：{set(list1)}")
print(f"元组 转集合：{set(tuple1)}")
print(f"字符串 转集合：{set(str1)}")
print(f"集合 转集合：{set(set1)}")
print(f"字典 转集合：{set(dict1)}")

# 没有键值对 无法转字典

# 4.容器排序 sorted(容器,reverse=True) 排序结果放在列表对象中
list1 = [71, 22, 63, 74, 15]
tuple1 = (71, 2, 533, 64, 15)
str1 = "Iven likes apple"
set1 = {12, 42, 37, 49, 15}
dict1 = {'Iven':99, 'rosenn':93, 'Starry':89}

print(f"列表 排序：{sorted(list1)}")
print(f"元组 排序：{sorted(tuple1)}")
print(f"字符串 排序：{sorted(str1)}")
print(f"集合 排序：{sorted(set1)}")
print(f"字典 排序：{sorted(dict1)}")

print(f"列表 反向排序：{sorted(list1, reverse=True)}")
print(f"元组 反向排序：{sorted(tuple1, reverse=True)}")
print(f"字符串 反向排序：{sorted(str1, reverse=True)}")
print(f"集合 反向排序：{sorted(set1, reverse=True)}")
print(f"字典 反向排序：{sorted(dict1, reverse=True)}")
```

### 字符串大小比较的方式
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407100014646.png)
```python
# 字符串按位比较 abd > abc ab > a  a > A K2 > K1 
print(f"abd大于abc，结果：{'abd' > 'abc'}")
print(f"ab大于a，结果：{'ab' > 'a'}")
print(f"a大于A，结果：{'a' > 'A'}")
print(f"K2大于K1，结果：{'K2' > 'K1'}")
```

## 第七章
### 函数的多返回值
```python
def test_return():
    return 1, 'hello', False
x, y, z = test_return()
print(x)
print(y)
print(z)
```

### 函数的多种参数使用形式
```python
# 1.位置参数 调用函数时根据函数定义的参数位置来传递函数
def user_info(name, age, gender):
    print(f"姓名是:{name}，年龄是：{age}，性别是{gender}")
user_info('Iven', 22, '男')

# 2.关键字参数 函数调用时你用键 = 值 形式来传递参数  参数位置可以并不固定 
# * 也可以混用 但混用时必须把位置参数放在关键词参数前面
user_info(age=22, gender='男', name='Iven')
user_info(gender='男', name='Iven', age=22)
user_info('Iven', gender='男', age=22)
# // user_info(name='Iven', '男', age=22)

# 3.缺省参数 为参数提供默认值
# * 默认值参数必须写在最后面
def user_info(name, age, gender='男'):
    print(f"姓名是:{name}，年龄是：{age}，性别是{gender}")
# // def user_info(name='iven', age, gender):
# //     print(f"姓名是:{name}，年龄是：{age}，性别是{gender}")
user_info(age=21, name='Rosenn')
user_info(age=21, name='Rosenn', gender='女')

# 4.不定长参数 可变参数 不确定调用时会传递多少参数 也可以不传递参数 
# 位置传递 *args 传递一个元组类型 一般叫args
def user_info(*args):
    print(f"args参数的类型是：{type(args)}，内容为{args}")
user_info(1, 2, 3, 'Iven', {'hello'})
# 关键字传递 **kwargs 键值 传递一个字典
def user_info(**kwargs):
    print(f"kwargs参数的类型是：{type(kwargs)}，内容为{kwargs}")
user_info(name='Iven', age=22, score=93, word={'hello'})
```

### 函数作为参数传递
```python
# 计算逻辑的传递 而非数据传递
def test_func(compute):
    result = compute(1, 2)
    print(f"compute参数的类型是：{type(compute)}，计算结果:{result}")

def compute(x, y):
    result = x + y
    return result

test_func(compute)
```

### lambda匿名函数
```python
# def 定义带有名称的函数 可以重复使用
# lambda 定义匿名函数 临时使用一次 lambda 传入参数: 函数体(一行代码) 只限一行代码
def test_func(compute):
    result = compute(1, 2)
    print(f"compute参数的类型是：{type(compute)}，计算结果:{result}")

test_func(lambda x, y: x + y)
```

## 第八章
### 文件编码概念
编码技术 翻译的规则 记录如何将内容翻译成二进制，以及如何将二进制翻译回识别内容 最常用UTF-8 还有GBK Big5等

### 文件的读取操作
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407101331600.png)
```python
# open(name, mode, encoding) 打开文件 mode 只读r、写入w、追加a
f = open("related_data/test.txt", "r", encoding="UTF-8")
print(type(f))

# read(num) num从文件中读取的数据长度(单位是字节) 不传入代表所有数据 返回字符串
# * 连续使用read读取 第二次read的部分会在第一次read结束位置接着读取 有读取指针
print(f"读取十个字节的结果：{f.read(10)}")
print(f"读取全部内容的结果：{f.read()}")

# readlines() 文件内容一次性读取，返回一个列表，每一行的数据为一个元素
f = open("related_data/test.txt", "r", encoding="UTF-8")
lines = f.readlines()
print(f"lines对象的类型：{type(lines)}，内容为{lines}")

# readline() 一次读取一行内容
f = open("related_data/test.txt", "r", encoding="UTF-8")
lines = f.readline()
print(f"第一行的类型：{type(lines)}，内容为{lines}")
lines = f.readline()
print(f"第二行的类型：{type(lines)}，内容为{lines}")
lines = f.readline()
print(f"第二行的类型：{type(lines)}，内容为{lines}")

# for循环读取
f = open("related_data/test.txt", "r", encoding="UTF-8")
for line in f:
    print(f"每一行的数据为：{line}")

# close()关闭文件 解除文件占用
f.close()
# import time 
# time.sleep(500000)

# with open 执行完相关语句自动关闭文件
with open("related_data/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行的数据为：{line}")
# import time 
# time.sleep(500000)

# 练习
# 第一种
count = 0
with open("related_data/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        count += line.count("Iven")
print(f"Iven出现的次数为:{count}")

# 第二种
count = 0
f = open("related_data/test.txt", "r", encoding="UTF-8")
test_str = f.read()
count += test_str.count("Iven")
print(f"Iven出现的次数为:{count}")
f.close()

# 第三种
count = 0
f = open("related_data/test.txt", "r", encoding="UTF-8")
test_list = f.readlines()
for element in test_list:
    count += element.count("Iven")
print(f"Iven出现的次数为:{count}")
f.close()

# 第四种
count = 0
f = open("related_data/test.txt", "r", encoding="UTF-8")
row = f.readline()
while row != "":
    count += row.count("Iven")
    row = f.readline()
print(f"Iven出现的次数为:{count}")
f.close()

# 第五种 有弊端 若无空格拆分不了
count = 0
f = open("related_data/test.txt", "r", encoding="UTF-8")
for line in f:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == "Iven":
            count += 1
print(f"Iven出现的次数为:{count}")
f.close()
```

### 文件的写入操作
```python
import time

# 设置test_write.txt不存在 自动创建文件
f = open("related_data/test_write.txt", "w", encoding="UTF-8")
# write 积攒在程序的内存中，又称为缓冲区  
f.write("Hello World!")
# // time.sleep(5000000)

# flush 内容刷新 刷新后内容才会真正写入文件
f.flush()
# // time.sleep(5000000)
# close内置flush功能
f.close()

#  若存在 写入操作会清空原文件
f = open("related_data/test_write.txt", "w", encoding="UTF-8")
# write 积攒在程序的内存中，又称为缓冲区  
f.write("Iven")
f.close()
```

### 文件的追加写入操作
```python
# 设置test_append.txt不存在 自动创建文件
f = open("related_data/test_append.txt", "a", encoding="UTF-8")
# write 积攒在程序的内存中，又称为缓冲区  
f.write("Hello World!")
f.flush()
f.close()

# 已有append文件
# 设置test_append.txt不存在 自动创建文件
f = open("related_data/test_append.txt", "a", encoding="UTF-8")
# write 积攒在程序的内存中，又称为缓冲区  
f.write("\nIven!")
f.flush()
f.close()
```
### 文件操作的综合案例
```python
f_r = open("related_data/bill.txt", "r", encoding="UTF-8")
f_w = open("related_data/bill.txt.bak", "w", encoding="UTF-8")

line = f_r.readline()
while line != "":
    if line.count("测试") == 0:
        f_w.write(line)
    line = f_r.readline()
f_w.flush()
f_r.close()
f_w.close()

f_r = open("related_data/bill.txt", "r", encoding="UTF-8")
f_w = open("related_data/bill.txt.bak", "r", encoding="UTF-8")
print(f"原数据为：\n{f_r.read()}")
print(f"备份好的数据为：\n{f_w.read()}")
f_r.close()
f_w.close()
```

## 第九章
### 了解异常
```python
# 异常bug：程序运行的过程中出现了错误
f = open("/abc.txt", "r", encoding="UTF-8")
# 发生异常: FileNotFoundError
# [Errno 2] No such file or directory: '/abc.txt'
#   File "D:\桌面\Coding\Python\060_了解异常.py", line 2, in <module>
#     f = open("/abc.txt", "r", encoding="UTF-8")
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: '/abc.txt'
```

### 异常的捕获
```python
# 捕获异常：提前假设某处出现异常，做好提前准备，当真的出现异常，可以有后续手段
# 基本捕获异常方法 try... except 捕获所有异常
try:
    f = open("related_data/error.txt", "r", encoding="UTF-8")
except:
    print("出现异常了，文件不存在，将以w模式打开，自动创建文件")
    f = open("related_data/error.txt", "w", encoding="UTF-8")

# 捕获指定异常  
try:
    # print(name)
    1 / 0
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

# 捕获多个异常
try:
    print(1 / 0)
    # print(name)
except (NameError, ZeroDivisionError) as e:
    print("ZeroDivision错误")

# 捕获所有异常 Exception 也可以直接用最基本的异常
try:
    # print(name)
    1 / 0
    # f = open("related_data/all_error.txt", "r", encoding="UTF-8")
except Exception as e:
    print("出现异常了")

# 异常else 没有异常执行 可选
try:
    # print(name)
    # 1 / 0
    # f = open("related_data/all_error.txt", "r", encoding="UTF-8")
    print("hello")
except Exception as e:
    print("出现异常了")
else:
    print("没有异常！")

# 异常finally 无论是否异常都执行 可选
try:
    f = open("related_data/error.txt", "r", encoding="UTF-8")
except Exception as e:
    print("出现异常了")
    f = open("related_data/error.txt", "w", encoding="UTF-8")
else:
    print("没有异常！")
finally:
    print("我是finally，有没有异常我都要执行")
    f.close()
```

### 异常的传递性
```python
def func1():
    print("func1开始")
    num = 1 /0
    print("func1开始")

def func2():
    print("func2开始")
    func1()
    print("func2开始")

def main():
    # 有传递性 可以在最高一层捕获最底一层出现的异常
    try:
        func2()
    except Exception as e:
        print(f"出现异常，异常信息是：{e}")

main()

# 传递性 由最底一层到最高层
# 发生异常: ZeroDivisionError
# division by zero
#   File "D:\桌面\Coding\Python\062_异常的传递性.py", line 3, in func1
#     num = 1 /0
#           ~~^~
#   File "D:\桌面\Coding\Python\062_异常的传递性.py", line 8, in func2
#     func1()
#   File "D:\桌面\Coding\Python\062_异常的传递性.py", line 12, in main
#     func2()
#   File "D:\桌面\Coding\Python\062_异常的传递性.py", line 14, in <module>
#     main()
# ZeroDivisionError: division by zero
```

### 模块的概念和导入
```python
# module
# [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]      []可选

# import 导入
# python 内置time.py 这个文件
import time
print("你好")
time.sleep(5)  # 通过.可以使用模块内部的全部功能（类、函数、变量）
print("我好")

# from 模块名 import 功能名  针对某个功能去使用
from time import sleep
print("你好")
sleep(5)  # 可以直接调用sleep
print("我好")

# 使用 * 导入模块所有功能 并可以直接调用 
from time import *
print("你好")
sleep(5)  # 可以直接调用sleep
print("我好")

# as 别名
import time as t
print("你好")
t.sleep(5)  # 可以直接调用sleep
print("我好")

from time import sleep as sl
print("你好")
sl(5)  # 可以直接调用sleep
print("我好")
```

### 自定义模块并导入
my_module1.py
```python
def test(a, b):
    print(a + b)

def test_1(a, b):
    print(a - b)

# 当自己运行时name=main 当被其他程序调用时则不是 不执行
if __name__ == '__main__':
    test(1, 2)
```

my_module1.py
```python
def test(a, b):
    print(a - b)
```

main.py
```python
import related_data.my_module1 as my_module1
my_module1.test(1, 2)

from related_data.my_module1 import test
test(1, 2)

# 同名功能后一个覆盖前一个
from related_data.my_module1 import test
from related_data.my_module2 import test
test(1, 2)

# 当自己运行时name=main 当被其他程序调用时则不是 不执行  便于测试自定义模块文件
# if __name__ == '__main__':
#     test(1, 2)

# 如果在module模块里定义了__all__ = ['test'] 则import * 只会导入all变量里的函数  但其他手动导入方法都可以 e.g import test_1
from related_data.my_module1 import *
test(1, 2)
# test_1(1, 2)
```

### 自定义Python包
__init__.py
```python
__all__ = ['my_module1']
```

my_module1.py
```python
def print1():
    print("我是模块1的功能代码")

```

my_module2.py
```python
def print2():
    print("我是模块2的功能代码")
```

main.py
```python
# Python包文件夹 包含一堆python模块和__init__.py
import related_data.my_package.my_module1
import related_data.my_package.my_module2

related_data.my_package.my_module1.print1()
related_data.my_package.my_module2.print2()

from related_data.my_package import my_module1
from related_data.my_package import my_module2
my_module1.print1()
my_module2.print2()

from related_data.my_package.my_module1 import print1
from related_data.my_package.my_module2 import print2
print1()
print2()

# 在包中添加__init_.py才能表示这是个python包，否则只是普通文件夹
# 在__init_.py中定义all变量 控制*选择的模块
from related_data.my_package import *
my_module1.print1()
# // my_module2.print2()
```

### 安装第三方包
```python
# 第三方包 非python官方内置的包 安装获得扩展功能 提升开发效率

# 直接安装
# pip install [包名]
# pip install -i [国内镜像网址]

# pycharm可以通过右下角解释器设置中搜索包并安装
```

### 异常_模块_包_综合案例讲解
__init__.py
```python

```

str_util.py
```python
def str_reverse(s):
    str_re = s[::-1]
    print(f"原字符串为：{s}")
    print(f"反转字符串为：{str_re}")
    return str_re

def substr(s, x , y):
    piece = s[x: y]
    print(f"原字符串为：{s}")
    print(f"字符串切片为：{piece}")
    return piece
```

file_util.py
```python
def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        print(f"原文件的全部内容:\n{f.read()}")
    except FileNotFoundError as e:
        print("文件不存在！")
    finally:
        # * 如果文件打开异常f.close()异常
        # 解决 在外面先定义f为None 后加if判断f类型
        if f:
            f.close()


def append_to_file(file_name, data):
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        print(f"原文件的全部内容:\n{f.read()}")
    except FileNotFoundError as e:
        print("文件不存在！")
    finally:
        # * 如果文件打开异常f.close()异常
        # 解决 在外面先定义f为None 后加if判断f类型
        if f:
            f.close()

    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.flush()
    f.close()

    f = open(file_name, "r", encoding="UTF-8")
    f.read()
    print(f"更新后文件的全部内容:\n{f.read()}")
```

main.py
```python
from related_data.my_utils import str_util
from related_data.my_utils import file_util

str_util.str_reverse('Iven enjoys coding')
str_util.substr('Iven enjoys coding', 3 , 9)

file_util.print_file_info('related_data/package.txt')
file_util.append_to_file('related_data/package.txt', 'Iven')
```

## 第十章 数据可视化 案例1：折线图
### json数据格式的转换
```python
"""
json 是一种轻量级数据交互格式 可以按照json指定的格式去组织和封装数据 
本质上是一个带有特定格式的字符串 
负责不同编程语言中的数据传递和交互 类似于国际通用语言 
"""

# 格式有两种 一种是字典 另一种是列表嵌套字典
import json

# dumps() 列表转json
# 若传入中文加入ensure_ascii=False 不使用ASCII码 直接传入
data = [{"name":"Iven", "age":"21"}, {"name":"Rosenn", "age":"18"}, {"name":"派大星", "age":"25"}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 字典转json
d = {"name":"Iven", "age":"21"}
json_str = json.dumps(d , ensure_ascii=False)
print(type(json_str))
print(json_str)

# loads() json转列表
s = '[{"name":"Iven", "age":"21"}, {"name":"Rosenn", "age":"18"}, {"name":"派大星", "age":"25"}]'
l = json.loads(s) 
print(type(l))
print(l)

# json转字典
d = '{"name":"Iven", "age":"21"}'
l = json.loads(d) 
print(type(l))
print(l)

```

### pyecharts模块简介
https://pyecharts.org/
echarts 产生可视化图表 
Echarts 是一个由百度开源的数据可视化，凭借着良好的交互性，精巧的图表设计，得到了众多开发者的认可。而 Python 是一门富有表达力的语言，很适合用于数据处理。当数据分析遇上数据可视化时，pyecharts 诞生了。
通过画廊可以复制粘贴相关图表的代码

### pyecharts入门使用
在069_render.html文件当中
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407112257176.png)
```python
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# Line() 创建一个折线图对象
line = Line()
# add_xaxis() 添加x轴的数据
line.add_xaxis(["中国", "美国", "英国"])
# add_yaxis() 添加y轴的数据
line.add_yaxis("GDP", [30, 20, 10])
# 全局配置选项 set_global_opts() 官网查看更多配置选项
line.set_global_opts(
    # 标题 title标题名 pos_left居中 pos_bottom靠近底部1%
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    # 图例 是否展示
    legend_opts=LegendOpts(is_show=True),
    # 工具箱 是否展示
    toolbox_opts=ToolboxOpts(is_show=True),
    # 视觉映射 是否展示
    visualmap_opts=VisualMapOpts(is_show=True)

)
# render() 将代码生成为图像
line.render()

# 全局配置 set_global_opts()
# 标题 图例 工具箱 
```
### 数据处理
```python
# www.ab173.com https://www.json.cn/jsononline/ json数据格式化
# * 这个更好用https://www.bejson.com/
import json

f_us = open("related_data/可视化案例数据/折线图数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
# 去除不属于json格式的错误部分
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
# json转字典
us_dict = json.loads(us_data)
print(us_dict)
print(type(us_dict))

# 取趋势字典
trend_data = us_dict['data'][0]['trend']
print(trend_data)
print(type(trend_data))

# 获取日期数据 只取2020年的数据 下标314 但不包括314
x_data = trend_data['updateDate'][:314]
print(x_data)

# 获取确诊数据 只取2020年的数据 下标314 但不包括314
y_data = trend_data['list'][0]['data'][:314]
print(y_data)
```
### 生成折线图
在071_render.html文件当中
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407120006071.png)
```python
# www.ab173.com https://www.json.cn/jsononline/ json数据格式化
# * 这个更好用https://www.bejson.com/
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# todo 美国
f_us = open("related_data/可视化案例数据/折线图数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
# 去除不属于json格式的错误部分
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
# json转字典
us_dict = json.loads(us_data)

# 取趋势字典
us_trend_data = us_dict['data'][0]['trend']

# 获取日期数据 只取2020年的数据 下标314 但不包括314
us_x_data = us_trend_data['updateDate'][:314]

# 获取确诊数据 只取2020年的数据 下标314 但不包括314
us_y_data = us_trend_data['list'][0]['data'][:314]

# todo 日本
jp_us = open("related_data/可视化案例数据/折线图数据/日本.txt", "r", encoding="UTF-8")
jp_data = jp_us.read()
# 去除不属于json格式的错误部分
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
jp_data = jp_data[:-2]
# json转字典
jp_dict = json.loads(jp_data)

# 取趋势字典
jp_trend_data = jp_dict['data'][0]['trend']

# 获取日期数据 只取2020年的数据 下标314 但不包括314
jp_x_data = jp_trend_data['updateDate'][:314]

# 获取确诊数据 只取2020年的数据 下标314 但不包括314
jp_y_data = jp_trend_data['list'][0]['data'][:314]

# todo 印度
in_us = open("related_data/可视化案例数据/折线图数据/印度.txt", "r", encoding="UTF-8")
in_data = in_us.read()
# 去除不属于json格式的错误部分
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
in_data = in_data[:-2]
# json转字典
in_dict = json.loads(in_data)

# 取趋势字典
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据 只取2020年的数据 下标314 但不包括314
in_x_data = in_trend_data['updateDate'][:314]

# 获取确诊数据 只取2020年的数据 下标314 但不包括314
in_y_data = in_trend_data['list'][0]['data'][:314]

# todo 生成图表
line = Line()
line.add_xaxis(us_x_data)
# label_opts 设置不显示y轴数字
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title='2020年美日印三国确诊人数对比折线图', pos_left='center', pos_bottom='1%'),
)
line.render()
```

## 第十一章 数据可视化 案例2：地图
### 基础地图使用
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407120927166.png)
```python
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
data = [
    ("北京市", 99),
    ("湖南省", 199),
    ("上海市", 299),
    ("台湾省", 399),
    ("广东省", 499)
]

# add() 图例 数据列表 地图类型
map.add("测试地图", data, "china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        # 是否显示视觉映射
        is_show=True, 
        # 是否允许手动校准范围/是否分段
        is_piecewise=True,
        # 设置颜色区间 最小值 最大值 区域标签 找到RGB16色代码
        pieces=[
            {"min":1, "max":9, "label":"1-9", "color":"#CCFFFF"},
            {"min":10, "max":99, "label":"10-9", "color":"#FF6666"},
            {"min":100, "max":500, "label":"100-500", "color":"#990033"},
        ]
        )
)
map.render("related_data/072_基础地图使用.html")
```

### 全国疫情地图构建
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407121007961.png)
```python
import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("related_data/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()

# 转字典
data_dict = json.loads(data)
# 取出省份数据
province_data_list = data_dict['areaTree'][0]['children']
# 组装每个省份和确诊人数为元组，将各个省的数据都封装在列表内
data_list = []
for province_data in province_data_list:
    # 省份名称 新版pyecharts必须写清楚省市
    if province_data["name"] == '北京' or province_data["name"] == '天津' or province_data["name"] == '上海' or province_data["name"] == '重庆':
        province_name = province_data["name"] + "市"
    elif province_data["name"] == '西藏' or province_data["name"] == '内蒙古':
        province_name = province_data["name"] + "自治区"
    elif province_data["name"] == '广西' :
        province_name = province_data["name"] + "壮族自治区"
    elif province_data["name"] == '新疆' :
        province_name = province_data["name"] + "维吾尔自治区"
    elif province_data["name"] == '宁夏' :
        province_name = province_data["name"] + "回族自治区"
    elif province_data["name"] == '香港' or province_data["name"] == '澳门':
        province_name = province_data["name"] + "特别行政区"
    else:
        province_name = province_data["name"] + "省"
    # 确诊人数
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))
print(data_list)

# 创建地图对象
map = Map()
# add() 图例 数据列表 地图类型
map.add("各省份确诊人数", data_list, "china")

map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000+人", "color": "#990033"},
        ]
    )
)
# 设置文件名
map.render("related_data/073_全国疫情地图.html")
```

### 河南省疫情地图绘制
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407121024076.png)
```python
import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("related_data/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()


# 转字典
data_dict = json.loads(data)
# 取出省份数据
henan_data_list = data_dict['areaTree'][0]['children'][3]['children']
# 组装每个省份和确诊人数为元组，将各个省的数据都封装在列表内
city_data_list = []
for city_data in henan_data_list:
    # 省份名称 新版pyecharts必须写清楚省市
    city_name = city_data["name"] + "市"
    # 确诊人数
    city_confirm = city_data["total"]["confirm"]
    city_data_list.append((city_name, city_confirm))
print(city_data_list)
# 手动添加济源市的数据
city_data_list.append(("济源市", 5))

# 创建地图对象
# add() 图例 数据列表 地图类型
map = Map()
map.add("河南省各市确诊人数", city_data_list, "河南")

map.set_global_opts(
    # title_opts 地图标题
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000+人", "color": "#990033"},
        ]
    )
)
# 设置文件名
map.render("related_data/074_河南省疫情地图.html")
```

## 第十二章 数据可视化 案例3：动态柱状图
### 基础柱状图构建
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407121039198.png)
```python
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
bar = Bar()

bar.add_xaxis(["中国", "美国", "英国"])
# 图例 数值 让数值位于图右侧
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))

# 翻转xy轴
bar.reversal_axis()
bar.render("related_data/075_基础柱状图.html")
```

### 基础时间线柱状图绘制
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407121443176.png)
```python
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 10, 50], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"],)
bar3.add_yaxis("GDP", [90, 40, 70], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 创建时间线 timeline对象 
# 设置时间线主题
timeline = Timeline({"theme": ThemeType.DARK})
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")

# 自动播放 add_schema()
timeline.add_schema(
    # 自动播放时间间隔 单位毫秒
    play_interval=1000,
    # 是否在自动播放时候, 显示时间线
    is_timeline_show=True,
    # 是否自动播放
    is_auto_play=True,
    # 是否循环自动播放
    is_loop_play=True
)

timeline.render("related_data/076_基础时间线柱状图.html")
```

### 动态GDP柱状图绘制
![](https://cdn.jsdelivr.net/gh/IvenStarry/Image/MarkdownImage/202407121446918.png)
```python
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts, TitleOpts
from pyecharts.globals import ThemeType

# todo 补充：列表的sort方法
# 列表.sort(key=排序函数, reverse=T/F
my_list = [["a", 33], ["b", 55], ["c", 88]]

# 第一种 def自定义函数
def choose_sort_key(element):
    return element[1]

my_list.sort(key=choose_sort_key, reverse=True)
# print(my_list)

# 第二种 lambda匿名函数
my_list.sort(key=lambda element: element[1], reverse=True)
# print(my_list)

# todo 数据处理
# csv编码格式 简体中文 GB2312
f = open("related_data/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
# 返回一个列表 每一行为一个元素
data_lines = f.readlines()
f.close()
# 删除表头行
data_lines.pop(0)

# 数据转换字典 格式：{年份：[[国家,gdp], [国家, gdp], ......], 年份：[[国家,gdp], [国家, gdp], ......],年份：[[国家,gdp], [国家, gdp], ......]}
data_dict = {}
for line in data_lines:
    year = int(line.split(',')[0])
    country = line.split(',')[1]
    # 科学计数法全部显示 转float类型
    gdp = float(line.split(',')[2])
    # 想要给年份的列表值用append前 列表必须有定义[] 才能继续添加新元素
    # my_dict = {}
    # my_dict['Iven']
    # 判断字典里有没有指定的Key值
    try:
        data_dict[int(year)].append([country, gdp])
    except KeyError:
        data_dict[int(year)] = []
        data_dict[int(year)].append([country, gdp])
# print(data_dict)

# todo 绘图
# 创建时间线对象 主题选择
timeline = Timeline({"theme":ThemeType.CHALK})
# 排序年份 防止字典读取混乱
sorted_year_list = sorted(data_dict.keys())
# print(sorted_year_list)

for year in sorted_year_list:
    data_dict[year].sort(key=lambda element:element[1], reverse=True)
    year_data = data_dict[year][:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0]) # 国家
        y_data.append(round(country_gdp[1] / 100000000, 1)) # gdp round()函数四舍五入只小数点后一位
    
    bar = Bar()
    # 为了让gdp最大的放在最上面 翻转年份和数据
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)",y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        # 图像标题
        title_opts=TitleOpts(title=f"{year}年全球前8GDP")
    )
    timeline.add(bar, str(year))

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
timeline.render("related_data/077_1960-2019全球GDP前8国家.html")
```