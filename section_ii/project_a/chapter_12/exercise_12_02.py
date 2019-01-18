# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_12_02.py
@time: 2019-01-18 21:35

12-2 游戏角色：
找一幅你喜欢的游戏角色位图图像或将一幅图像转换为位图。
创建一个类，将该角色绘制到屏幕中央，并将该图像的背景色设置为屏幕背景色，
或将屏幕背景色设置为该图像的背景色

"""
import pygame

from python_helloworld.section_ii.project_a.chapter_12.example.bird import Bird
import python_helloworld.section_ii.project_a.chapter_12.example\
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_12.example.settings \
    import Settings


def create_pywindow():
    """创建一个背景为蓝色的Pygame窗口"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption("Birds")
    bird = Bird(screen)
    # 开始游戏的主循环
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, bird)


create_pywindow()
