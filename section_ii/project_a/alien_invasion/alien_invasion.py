# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: alien_invasion.py
@time: 2019-01-18 10:40

"""

import pygame

import python_helloworld.section_ii.project_a.alien_invasion.game_functions \
    as gf
from python_helloworld.section_ii.project_a.alien_invasion.settings \
    import Settings
from python_helloworld.section_ii.project_a.alien_invasion.ship \
    import Ship


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)


run_game()
