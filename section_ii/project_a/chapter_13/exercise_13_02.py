# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_13_02.py
@time: 2019-01-20 13:20

13-2 更逼真的星星：
为让星星的分布更逼真，可随机地放置星星。本书前面说过，可像下面这样来生成随机数：

from random import randint
random_number = randint(-10,10)

上述代码返回一个-10和10之间的随机整数。
在为完成练习13-1而编写的程序中，随机地调整每颗星星的位置。

"""
import pygame
import python_helloworld.section_ii.project_a.chapter_13.example_2\
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_13.example_2.settings \
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
