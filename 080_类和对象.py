# 使用类的属性和行为 可以描述现实世界的一切事物
# 面向对象编程： 使用对象进行编程 设计类 基于类创建对象 使用对象完成功能开发
# 类是程序中的设计图纸 对象是基于图纸生产的具体实体

class Clock:
    id = None
    price = None
    
    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

# 构建对象
clock1 = Clock()
clock1.id = "01234"
clock1.price = 19.99
print(f"闹钟ID:{clock1.id}，价格:{clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "01254"
clock2.price = 21.99
print(f"闹钟ID:{clock2.id}，价格:{clock2.price}")
clock2.ring()