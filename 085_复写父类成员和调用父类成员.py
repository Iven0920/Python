# 复写 子类继承父类的成员属性和成员方法后，如果对其不满意。可以进行重新定义
class Phone():
    IMEI = None
    producer = "Iven"
    
    def call_by_5g(self):
        print("父类单核5g通话")

class MyPhone(Phone):
    producer = "Rosenn"

    def call_by_5g(self):
        print("子类多核5g通话")

phone = MyPhone()
phone.call_by_5g()

# 调用父类同名成员
class Phone():
    IMEI = None
    producer = "Iven"
    
    def call_by_5g(self):
        print("使用5g通话")

class MyPhone(Phone):
    producer = "Rosenn"

    def call_by_5g(self):
        print("开启CPU单核模式")

        # 方法1： 父类名.成员变量/成员方法(self)
        print(f"父类的厂商是:{Phone.producer}")
        Phone.call_by_5g(self)

        # 方法2： super().成员变量/成员方法()
        print(f"父类的厂商是:{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式")

phone = MyPhone()
phone.call_by_5g()