# coding=utf-8
import pygame
import time
from pygame.locals import *
import random


class Base(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y  # 初始化玩家飞机的位置
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)


class BasePlane(Base):
    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self, screen_temp, x, y, image_name)
        self.bullet_list = []  # 用来存储发射出去的子弹对象引用。

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界。
                self.bullet_list.remove(bullet)


class HeroPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 210, 700, "./feiji/hero1.png")

    def move_left(self):
        self.x -= 15

    def move_right(self):
        self.x += 15

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))  # 调用飞机screen方法也可以完成方法调用。


class EnemyPlane(BasePlane):
    """# 6.1定义一个敌机的类"""
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 100, 0, "./feiji/enemy0.png")
        self.direction = "right"  # 用来存储飞机的默认的显示方向。

    def move(self):

        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self.x > 430:  # 这个数值取决于飞机的宽度：屏幕宽减去飞机宽。
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 78 or random_num == 88:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))  # 调用飞机screen方法也可以完成方法调用。


class BaseBullet(Base):
    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self, screen_temp, x, y, image_name)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet .__init__(self, screen_temp, x+40, y-20, "./feiji/bullet.png")

    def move(self):
        self.y -= 5  # 让子弹飞起来。当然此处与time(0.01)配合使用来控制速度。

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 25, y + 40, "./feiji/bullet1.png")

    def move(self):
        self.y += 5  # 让子弹飞起来。当然此处与time(0.01)配合使用来控制速度。

    def judge(self):
        if self.y > 850:
            return True
        else:
            return False


def key_control(hero_temp):
    # 5.检测键盘
    #     通过键盘检测来控制触发事件进而实现图像对键盘的响应。
    #     获取事件，比如按键等。
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮：
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                hero_temp.move_left()
                print("left")

            # 检测案件是否是d或者是right
            elif event.key == K_d or event.key == K_RIGHT:
                hero_temp.move_right()
                print("right")

            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                hero_temp.fire()
                print("space")


def main():
    # 1.创建一个窗口，用来显示内容。
    screen = pygame.display.set_mode((480, 752), 0, 32)

    # 2.创建一个和窗口大小相同的照片，用来充当背景。
    background = pygame.image.load("./feiji/background.png")

    # 4.创建一个飞机对象
    hero = HeroPlane(screen)

    # 6.2创建一个敌机
    enemy = EnemyPlane(screen)

    while True:
        # 3.把背景图片放到窗口中显示。
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))    # 将图片贴到窗口中，图片左上角的原点，贴到窗口的原点。

        # 4.1将飞机图片显示出来：
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()

        # 更新需要显示的内容
        pygame.display.update()   # 把内存中的数据显示到屏幕上。
        key_control(hero)
        time.sleep(0.01)  # 将显示界面驻留在窗口上，但不希望一直执行，降低CPU占用。


if __name__ == '__main__':
    main()
