# 从零开始学Python
学习视频网站：B站黑马程序员
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