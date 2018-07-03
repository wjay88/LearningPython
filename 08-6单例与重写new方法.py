# class Dog(object):
#     def __init__(self):
#         print("---init方法----")
#
#     def __str__(self):
#         print("---str方法----")
#         return "对象描述信息"
#
#     def __del__(self):
#         print("---del方法----")
#
#     def __new__(cls, *args, **kwargs):
#         print("---new方法----")
#         return object.__new__(cls)
#
#
# xtq = Dog()
# print(xtq)


# 构造方法的概念：
# 既有初始化又有新建。python中将其分为两步。
# 1、调用__new__方法类创建对象，然后找一个变量来接收__new__的返回值，这个返回值表示创建出来的对象的引用
# 2、__init__（刚刚创建出来的对象的应用。）初始化。
# 3、返回对象的引用。
#
# 重写__new__方法的原因。


# 单例对象的创建
#
# class Dog(object):
#     pass
#
# a = Dog()
# b = Dog()
# a和b指向同一个对象就是单例。如何实现？过程与新建对象方法有关，想到__new__方法。所以重写__new__方法。
class Dog():

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, name):
        self.name = name


a = Dog("旺财")
print(id(a))
print(a.name)

b = Dog("哮天犬")
print(id(b))
print(b.name)

为了防止两次print都执行，将__init__修改为：
# def __init__(self,name):
#     if Dog.__init_flag == False
#     self.name = name
#     Dog.__init_flag = True