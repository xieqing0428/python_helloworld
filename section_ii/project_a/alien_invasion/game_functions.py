# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: game_functions.py
@time: 2019-01-18 21:10

存储大量让游戏《外星人入侵》运行的函数

"""
import sys
import pygame


def check_events():
    """相应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
