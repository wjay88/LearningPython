# python 实现功能：老王拿枪打敌人的操作。


class Person(object):
    """人的类"""
    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name
        self.gun = None # 用来保存枪对象的引用。、
        self.hp = 100

    def anzhuang_zidan(self, dan_jia_temp, zi_dan_temp):
        """把子弹装到弹夹中"""

        # 弹夹，保存子弹（子弹），所以弹夹要有一个保存子弹的功能。
        dan_jia_temp.baocun_zidan(zi_dan_temp)

    def anzhuang_danjia(self, gun_temp, dan_jia_temp):
         """把弹夹安装到枪中"""
         # 枪.保存弹夹（弹夹）
         gun_temp.baocun_danjia(dan_jia_temp)

    def naqiang(self, gun_temp):
        """拿起一把枪：何为拿起一把枪，带一个属性。有枪"""
        self.gun = gun_temp

    def __str__(self):
        if self.gun:
            return "%s的血量为：%s, 他有枪，%s" % (self.name, self.hp, self.gun)
        else:
            if self.hp > 0:
                return "%s的血量为：%s,他没有枪" % (self.name,self.hp)
            else:
                return "%s已挂" % self.name

    def kou_ban_ji(self, diren):
        """让枪发射子弹，打敌人。"""
        self.gun.fire(diren)

    def diao_xue(self, sha_shang_li):
        """根据杀伤力，掉相应的血量"""
        self.hp -= sha_shang_li


class Gun(object):
    """枪的类"""
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name  # 用来记录枪的类型
        self.danjia = None

    def baocun_danjia(self,dan_jia_temp):
        """用一个属性来保存这个弹夹"""
        self.danjia = dan_jia_temp

    def __str__(self):
        if self.danjia:
            return "枪的信息为：%s,%s" % (self.name, self.danjia)
        else:
            return "枪的信息为：%s,这把枪中没有弹夹" % self.name

    def fire(self, diren):
        """枪从弹夹中获取一发子弹，然后让这发子弹击中敌人："""
        # 先从弹夹中去子弹。让弹夹有个功能：弹出一发子弹。所以：去弹夹类中增加功能。、
        zidan_temp = self.danjia.tanchu_zidan()
        # 让这个子弹去伤害敌人
        if zidan_temp:
            # 子弹打中敌人（敌人）
            zidan_temp.dazhong(diren)
        else:
            print("弹夹中没有子弹了。。。。")


class Danjia(object):
    """弹夹的类"""
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num  # 用来记录弹夹的最大容量。
        self.zidan_list = []  # 用来记录所有子弹的引用。

    def baocun_zidan(self, zi_dan_temp):
        # 将这个子弹保存
        # 一个对象保存另一个对象，找一个属性，能有包含功能。列表包含另一个对象引用。
        # 列表可以包含多个对象，所以弹夹多定义一个属性。在__init__中定义新属性。
        self.zidan_list.append(zi_dan_temp)

    def __str__(self):
        """描述信息"""
        return "弹夹的信息为：%d/%d" % (len(self.zidan_list), self.max_num)

    def tanchu_zidan(self):
        """弹出最上面的那颗子弹"""   # 先进后出
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None


class Zidan(object):
    """子弹的类"""
    def __init__(self, sha_shang_li):
        self.sha_shang_li = sha_shang_li

    def dazhong(self, diren):
        """让敌人掉血"""
        # 敌人.掉血（一颗子弹的威力），又转回到人了。
        diren.diao_xue(self.sha_shang_li)


def main():
    """用来控制整个程序的流程："""
    # pass

    # 1、创建老王对象：
    laowang = Person("老王")

    # 2、创建一个枪对象：
    ak47 = Gun("AK47")

    # 3、创建一个弹夹对象：
    dan_jia = Danjia(20)

    # 4、创建一些子弹对象：
    for i in range(15):
        zi_dan = Zidan(10)
        # 用面向对象来写重复执行的话，只需要加个for就能实现，特别简单。
        # 不用考虑具体怎么做，流程理清就好了。

        # ####对象创建、方法实现、一环套一环、转来转去########

        # 5、老王将子弹安装到弹夹：
            # 老王.安装子弹到弹夹中（弹夹、子弹）。
        laowang.anzhuang_zidan(dan_jia, zi_dan)

    # 6、老王把弹夹组装到枪上：
    # 老王安装弹夹到枪中（枪，弹夹）：
    laowang.anzhuang_danjia(ak47, dan_jia)

    # ========>>>此处开始就功能此时。
    # 测试弹夹和枪。因为上一步复杂度高。

    #     test
    print(dan_jia)
    print(ak47)

    # 7、老王拿起枪：

    laowang.naqiang(ak47)
    # test:测试老王对象：其实就是把对象属性信息打印一下。
    print(laowang)

    # 8、创建一个敌人对象：
    gebi_laosong = Person('隔壁老宋')
    print(gebi_laosong)

    # 9、老王开枪射击\打敌人：
    # 老王.扣扳机（隔壁老宋），开枪
    laowang.kou_ban_ji(gebi_laosong)
    print(gebi_laosong)
    print(laowang, '\n')  # 子弹是不是少了一颗。

    laowang.kou_ban_ji(gebi_laosong)
    print(gebi_laosong)
    print(laowang, '\n')  # 子弹是不是少了一颗。

    laowang.kou_ban_ji(gebi_laosong)
    print(gebi_laosong)
    print(laowang, '\n')  # 子弹是不是少了一颗。
    for i in range(7):
        laowang.kou_ban_ji(gebi_laosong)
        print("老王开枪-------->>隔壁老宋中枪。")
        print(gebi_laosong)
        print(laowang, '\n')  # 子弹是不是少了一颗。


if __name__ == '__main__':
    main()


# 案例最想表达的含义：一个对象创建出来之后，如果别的对象他想要去用这个对象，
# 仅仅需要在对象中创建一个属性指向这个对象的引用，那么就可以找到这个对象。

