# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_13_03.py
@time: 2019-01-20 13:50

13-3 雨滴：
寻找一幅雨滴图像，并创建一系列整齐排列的雨滴。让这些雨滴往下落，直到到达屏幕底端后消失

"""
import pygame
import python_helloworld.section_ii.project_a.chapter_13.example_3\
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_13.example_3.settings \
    import Settings
from pygame.sprite import Group


def run_game():
    pygame.init()
    rain_settings = Settings()
    screen = pygame.display.set_mode((rain_settings.screen_width,
                                      rain_settings.screen_height))
    pygame.display.set_caption("Rain")

    rains = Group()

    gf.create_fleet(rain_settings, screen, rains)

    while True:
        gf.check_events()
        gf.update_rains(rain_settings, rains)
        gf.update_screen(rain_settings, screen, rains)


run_game()
