# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: alien_invasion.py
@time: 2019-01-18 10:40

"""
import pygame

import python_helloworld.section_ii.project_a.alien_invasion.game_functions \
    as gf
from pygame.sprite import Group
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
    ship = Ship(ai_settings, screen)

    # 创建子弹编组
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
