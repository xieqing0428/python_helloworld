# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_14_03.py
@time: 2019-01-21 21:02

14-3 有一定难度的射击练习：
以你为完成练习14-2而做的工作为基础，让标靶的移动速度随游戏进行而加快，
并在玩家单击Play按钮时将其重置为初始值

"""
import pygame
from pygame.sprite import Group

import python_helloworld.section_ii.project_a.chapter_14.example_3 \
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_14.example_3.button \
    import Button
from python_helloworld.section_ii.project_a.chapter_14.example_3.game_stats \
    import GameStats
from python_helloworld.section_ii.project_a.chapter_14.example_3.rectangle \
    import Rectangle
from python_helloworld.section_ii.project_a.chapter_14.example_3.settings \
    import Settings
from python_helloworld.section_ii.project_a.chapter_14.example_3.ship \
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
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建子弹编组
    bullets = Group()
    rectangle = Rectangle(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship,
                        rectangle, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, stats, rectangle, bullets)
            gf.update_rectangle(ai_settings, rectangle)
        gf.update_screen(ai_settings, screen, stats, ship, rectangle, bullets,
                         play_button)


run_game()
