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