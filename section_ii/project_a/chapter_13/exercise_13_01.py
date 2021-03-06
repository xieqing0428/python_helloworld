# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_13_01.py
@time: 2019-01-19 22:44

13-1 星星：
找一幅星星图像，并在屏幕上显示一系列整齐排列的星星

"""
import pygame
import python_helloworld.section_ii.project_a.chapter_13.example_1\
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_13.example_1.settings \
    import Settings
from pygame.sprite import Group


def run_game():
    pygame.init()
    star_settings = Settings()
    screen = pygame.display.set_mode((star_settings.screen_width,
                                      star_settings.screen_height))
    pygame.display.set_caption("Star")

    stars = Group()

    gf.create_fleet(star_settings, screen, stars)

    while True:
        gf.check_events()
        gf.update_screen(star_settings, screen, stars)


run_game()




