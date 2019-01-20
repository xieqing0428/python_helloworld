# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_13_04.py
@time: 2019-01-20 14:51

13-4 连绵细雨：
修改为完成练习13-3而编写的代码，使得一行雨滴消失在屏幕底端后，
屏幕顶端又出现一行新雨滴，并开始往下落

"""
import pygame
import python_helloworld.section_ii.project_a.chapter_13.example_4\
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_13.example_4.settings \
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
        gf.update_rains(rain_settings, screen, rains)
        gf.update_screen(rain_settings, screen, rains)


run_game()
