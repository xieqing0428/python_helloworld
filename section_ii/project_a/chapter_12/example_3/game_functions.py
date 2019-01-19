# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: game_functions.py
@time: 2019-01-19 15:56

"""
import sys
import pygame


KEY_DOWN = True
KEY_UP = False


def check_events(rocket):
    """检查事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_events(event, rocket, KEY_DOWN)
        elif event.type == pygame.KEYUP:
            check_key_events(event, rocket, KEY_UP)


def check_key_events(event, rocket, key):
    """检查按键/松开"""
    if event.key == pygame.K_UP:
        rocket.moving_up = key
    if event.key == pygame.K_DOWN:
        rocket.moving_down = key
    if event.key == pygame.K_LEFT:
        rocket.moving_left = key
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = key


def update_screen(rocket_settings, screen, rocket):
    # 重绘填充背景色
    screen.fill(rocket_settings.bg_color)
    # 放置火箭
    rocket.blitme()
    # 展示
    pygame.display.flip()
