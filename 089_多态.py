# 多态:多种状态 
# 完成某个行为时，使用不同的对象会得到不同的状态
# 同样的行为 传入不同的对象 得到不同的状态

class Animal():
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵")

def make_noise(animal: Animal) -> str:
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

# 抽象类（接口）：含有抽象方法的类称之为抽象类
# 抽象方法： 方法体是空实现的(pass)称之为抽象方法
# 父类来确定有哪些方法 具体方法实现由子类自行决定 顶层设计与底层具体实现
class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_r_wind(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r_wind(self):
        print("美的空调左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r_wind(self):
        print("格力空调左右摆风")

def make_cool(ac:AC):
    ac.cool_wind()
    ac.hot_wind()
    ac.swing_l_r_wind()

midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)