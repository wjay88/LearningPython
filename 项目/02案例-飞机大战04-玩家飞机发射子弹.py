# coding=utf-8
import pygame
import time
from pygame.locals import *


class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 205
        self.y = 600    # 初始化玩家飞机的位置
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = []  # 用来存储发射出去的子弹对象引用。

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_left(self):
        self.x -= 15

    def move_right(self):
        self.x += 15

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))  # 调用飞机screen方法也可以完成方法调用。


class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5  # 让子弹飞起来。当然此处与time(0.01)配合使用来控制速度。


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
    while True:
        # 3.把背景图片放到窗口中显示。
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))    # 将图片贴到窗口中，图片左上角的原点，贴到窗口的原点。

        # 4.1将飞机图片显示出来：
        hero.display()
        # 更新需要显示的内容
        pygame.display.update()   # 把内存中的数据显示到屏幕上。
        key_control(hero)
        time.sleep(0.01)  # 将显示界面驻留在窗口上，但不希望一直执行，降低CPU占用。


if __name__ == '__main__':
    main()