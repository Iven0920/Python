# 继承
# 单继承 class 子类名(父类名):
class Phone():
    IMEI = None
    producer = "Iven"
    
    def call_by_4g(self):
        print("4g通话")

class Phone2024(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2024新功能：5g通话")

iphone = Phone2024()
iphone.call_by_4g()
iphone.call_by_5g()


# 多继承 class 子类名(父类名1, 父类名2, 父类名3,...)
# 继承顺序：左边最高 右边最低
# 在多个父类中，如果有同名的成员，先继承的保留，后继承的被覆盖，默认以继承顺序为优先级
class Phone():
    IMEI = None
    producer = "Iven"
    
    def call_by_4g(self):
        print("4g通话")

class NFCReader():
    nfc_type = "第五代"
    producer = "Rosenn"

    def read_card(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    re_type = "红外遥控"

    def control(self):
        print("红外遥控开始了")

class MyPhone(Phone, NFCReader, RemoteControl):
    # 通过关键字pass来补充语法上的不完整 实际无任何意义
    pass

phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

print(phone.producer)