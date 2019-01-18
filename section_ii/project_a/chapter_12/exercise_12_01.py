# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_12_01.py
@time: 2019-01-17 22:08

12-1 蓝色天空：
创建一个背景为蓝色的Pygame窗口

"""
import sys
import pygame


def create_pywindow():
    """创建一个背景为蓝色的Pygame窗口"""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("E.T")

    # 开始游戏的主循环
    while True:
        # 相应按键和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 255))
        # 让最近绘制的屏幕可见
        pygame.display.flip()


create_pywindow()
