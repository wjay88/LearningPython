# coding=utf-8
import pygame
import time

"""
    1、搭建界面，主要完成窗口和背景图的显示。
"""


def main():
    # 1.创建一个窗口，用来显示内容。
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2.创建一个和窗口大小相同的照片，用来充当背景。
    background = pygame.image.load("./feiji/background.png")

    # 3.把背景图片放到窗口中显示。
    while True:

        # 设定需要显示的背景图
        screen.blit(background, (0, 0))    # 将图片贴到窗口中，图片左上角的原点，贴到窗口的原点。

        # 更新需要显示的内容
        pygame.display.update()   # 把内存中的数据显示到屏幕上。

        time.sleep(0.5)  # 将显示界面驻留在窗口上，但不希望一直执行，降低CPU占用。










if __name__ == '__main__':
    main()

