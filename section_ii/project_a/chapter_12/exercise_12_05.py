# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_12_05.py
@time: 2019-01-19 17:26

12-5 侧面射击：
编写一个游戏，将一艘飞船放在屏幕左边，并允许玩家上下移动飞船。
在玩家按空格键时，让飞船发射一颗在屏幕中向右穿行的子弹，并在子弹离开屏幕而消失后将其删除

"""
import pygame
import python_helloworld.section_ii.project_a.chapter_12.example_5\
    .game_functions as gf
from pygame.sprite import Group

from python_helloworld.section_ii.project_a.chapter_12.example_5.settings \
    import Settings
from python_helloworld.section_ii.project_a.chapter_12.example_5.ufo import UFO


def run_game():
    pygame.init()
    ufo_settings = Settings()
    screen = pygame.display.set_mode(
        (ufo_settings.screen_width, ufo_settings.screen_height))
    pygame.display.set_caption("侧面射击")

    # 创建UFO对象
    ufo = UFO(ufo_settings, screen)

    # 创建子弹编组
    bullets = Group()

    while True:
        gf.check_events(ufo_settings, screen, ufo, bullets)
        ufo.update()
        gf.update_bullet(ufo, bullets)
        gf.update_screen(ufo_settings, screen, ufo, bullets)


run_game()

