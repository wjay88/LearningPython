# 通过Factory来实现了Car和CarStore的分离。通过一个类来实现一个类跟另一个类的分离。这就叫做简单工厂模式。
# 京东推荐：《Python设计模式》
# 通过一个类，完成两个类或者多个类之间的解耦。
# 编程设计思想包含了大量现代管理学方法！！！！

'''
设计一个北京现代的4S店。
'''

class CarStroe(object):

    def __init__(self):
        self.factory = Factory()

    def order(self, car_type):
        return self.factory.select_car_by_type(car_type)


class Factory(object):

    def select_car_by_type(self, car_type):
        if car_type == "索纳塔":
            return Suonata()
        elif car_type == "名图":
            return Mingtu()


class Car(object):
    def move(self):
        print('车在移动。。。。')

    def music(self):
        print('车在播放音乐。。。。')

    def stop(self):
        print('车在停止。。。。')

class Suonata(Car):
    pass

class Mingtu(Car):
    pass


car = Car()
car_store = CarStroe()
car = car_store.order('索纳塔')
car.move()
car.music()
car.stop()


# 新的问题，如果新建一个其他品牌的店铺：宝马的4S店。
# 新定义：一个新的类，可以直接复制原来的代码。

# 建立一个基类：Store
class Store(object):
    def select_car(self):
        pass

    def order(self,car_type):
        return self.select_car(car_type)

class BMWCarStore(Store):
    def select_car(self,car_type):
        return BMWFactory().select_car_by_type(car_type)

class CarStore(Store):
    def select_car(self,car_type):
        return Factory().select_car_by_type(car_type)

bmw_store = BMWcarStore()
# 基类定义指向，不涉及具体方法，具体功能和设计方法，有子类去慢慢实现。
# 这样子称为：工厂方法模式。
