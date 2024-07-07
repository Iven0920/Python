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