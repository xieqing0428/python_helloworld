# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_12_04.py
@time: 2019-01-19 15:00

12-4 按键：
创建一个程序，显示一个空屏幕。
在事件循环中，每当检测到pygame.KEYDOWN事件时都打印属性event.key。
运行这个程序，并按各种键，看看Pygame如何响应

"""
import sys
import pygame


def create_pywindow():
    """创建一个背景为白色的Pygame窗口"""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("exercise_12_04")

    # 开始游戏的主循环
    while True:
        # 相应按键和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event.key)
        screen.fill((255, 255, 255))
        # 让最近绘制的屏幕可见
        pygame.display.flip()


create_pywindow()
