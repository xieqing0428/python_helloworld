# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: game_functions.py
@time: 2019-01-18 22:52

"""
import sys
import pygame


def check_events():
    """相应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, bird):
    screen.fill(ai_settings.bg_color)
    bird.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
