# 面向对象三大特性 封装 继承 多态

# 封装 将现实世界在类中描述为属性和方法，即为封装
# 私有成员变量、私有成员方法： __变量名/方法名
# 类对象五大访问私有成员
# 类中其他成员可以访问私有成员
class Phone:

    __current_voltage = 0.5

    def __keep_single_core(self):
        print("让CPU以单核模式运行")
    
    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并以设置为单核运行进行声带你")


phone = Phone()
# 不可以调用私有成员
# // print(phone.__current_voltage)
# // phone.__keep_single_core()
phone.call_by_5g()

# 练习
class Phone:

    __is_5g_enable = False
    
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，是哦那个4g网络")
    
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

iphone = Phone()
iphone.call_by_5g()