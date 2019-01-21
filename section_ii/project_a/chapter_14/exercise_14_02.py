# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_14_02.py
@time: 2019-01-21 21:02

14-2 射击练习：
创建一个矩形，它在屏幕右边缘以固定的速度上下移动。
然后，在屏幕左边缘创建一艘飞船，玩家可上下移动该飞船，并射击前述矩形目标。
添加一个用于开始游戏的Play按钮，在玩家三次未击中目标时结束游戏，并重新显示Play按钮，
让玩家能够通过单击该按钮来重新开始游戏

"""
import pygame
from pygame.sprite import Group

import python_helloworld.section_ii.project_a.chapter_14.example_2 \
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_14.example_2.button \
    import Button
from python_helloworld.section_ii.project_a.chapter_14.example_2.game_stats \
    import GameStats
from python_helloworld.section_ii.project_a.chapter_14.example_2.rectangle \
    import Rectangle
from python_helloworld.section_ii.project_a.chapter_14.example_2.settings \
    import Settings
from python_helloworld.section_ii.project_a.chapter_14.example_2.ship \
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
            gf.update_bullets(stats, rectangle, bullets)
            gf.update_rectangle(ai_settings, rectangle)
        gf.update_screen(ai_settings, screen, stats, ship, rectangle, bullets,
                         play_button)


run_game()
