# class Dog:
#     pass
#
#
# dog = Dog()
# dog.age = 10
# dog.name = "小白"
#
# dog.get_age()
# dog.get_name()
# 用函数可以增加判断条件。设置属性函数时，增加判断。

# 完整模式：
class Dog:
    def set_age(self, new_age):
        if new_age > 0 and new_age <= 100:
            self.age = new_age
        else:
            self.age = 0

    def get_age(self):
        return self.age


dog = Dog()
dog.set_age(10)
age = dog.get_age()
print(age)
# 获取属性，尽量用函数(方法)来调用获取属性。这样避免任何人都能随便调用属性，保护核心数据不被外界人员读取。



# 私有化方法：
# 类似于隐藏属性，核心功能操作：比如收费业务需增加判断，不能直接执行的。

class TestSys:
    # 私有化方法：        核心功能或者收费功能。
    def __send_msg(self):
        print("--------正在发送短信---------")


    # 公有方法
    def send_msg(self, new_money):
        if new_money > 10000:       # 或者判断角色是否有权限操作。
            self.__send_msg()
        else:
            print("智商余额不足，请及时充值。")


test = TestSys()
test.send_msg(10000000)
# 通过公有方法，增加验证条件或角色判断，检测之后再执行核心功能。



