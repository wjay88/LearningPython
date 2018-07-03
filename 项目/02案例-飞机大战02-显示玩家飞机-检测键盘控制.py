# coding=utf-8
import pygame
import time
from pygame.locals import *

"""
    1、搭建界面，主要完成窗口和背景图的显示。
"""


def main():
    # 1.创建一个窗口，用来显示内容。
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2.创建一个和窗口大小相同的照片，用来充当背景。
    background = pygame.image.load("./feiji/background.png")

    # 4.11初始化玩家飞机的位置
    x = 205
    y = 700

    # 4.创建一个飞机图片
    hero = pygame.image.load("./feiji/hero1.png")
    while True:
        # 3.把背景图片放到窗口中显示。
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))    # 将图片贴到窗口中，图片左上角的原点，贴到窗口的原点。

        # 4.1将飞机图片显示出来：
        screen.blit(hero, (x, y))
        # 更新需要显示的内容
        pygame.display.update()   # 把内存中的数据显示到屏幕上。

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
                    x -= 12
                    print("left")

                # 检测案件是否是d或者是right
                elif event.key == K_d or event.key == K_RIGHT:
                    x += 15
                    print("right")

                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print("space")

        # 更新需要显示的内容
        pygame.display.update()

        time.sleep(0.01)  # 将显示界面驻留在窗口上，但不希望一直执行，降低CPU占用。


if __name__ == '__main__':
    main()
