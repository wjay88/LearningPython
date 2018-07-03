# 把一个对象放在另一个对象中。


class Home:
    def __init__(self, new_area, new_info, new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.cotain_items = []

    def __str__(self):
        msg =  "房子的总面积是：%d,可用面积是：%d,户型是：%s,地址是：%s" % (self.area, self.left_area, self.info, self.addr)
        msg += "当前房子里的东西有:%s" % str(self.cotain_items)
        return msg

    def add_item(self, item):
        # self.left_area -= item.area   # 此处是要重点理解记忆的。
        # self.cotain_items.append(item.name)
        self.left_area -= item.get_area()  # 以后统统直接获取属性的地方，改为获取方法。保护数据安全性。
        self.cotain_items.append(item.get_name())

class Bed:
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return "%s占用的面积是：%d" % (self.name, self.area)

    def get_area(self):
        return self.area
    # 直接获取属性的方式改为方法的原因：隐藏对象的属性和保护属性。

    def get_name(self):
        retun self.name


fangzi = Home(129, "三室一厅", "北京市 朝阳区 长安街 666号")
print(fangzi)

# 创建一个对象，首先要有一个类。
bed1 = Bed("席梦思", 4)
print(bed1)

# 要把床搬进房子。
# 房子有装床的功能。所以在房子中添加一个功能。

fangzi.add_item(bed1)
print(fangzi)

bed2 =Bed("三人床", 5)

fangzi.add_item(bed2)
print(fangzi)