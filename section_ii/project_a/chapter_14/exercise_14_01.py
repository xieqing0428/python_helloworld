# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_14_01.py
@time: 2019-01-21 20:47

14-1 按P开始新游戏：
鉴于游戏《外星人入侵》使用键盘来控制飞船，最好让玩家也能够通过按键来开始游戏。
请添加让玩家在按P时开始游戏的代码。
也许这样做会有所帮助：将check_play_button()的一些代码提取出来，
放到一个名为start_game()的函数中，
并在check_play_button()和check_keydown_events()中调用这个函数

"""
import pygame
from pygame.sprite import Group

import python_helloworld.section_ii.project_a.chapter_14.example_1\
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_14.example_1.button \
    import Button
from python_helloworld.section_ii.project_a.chapter_14.example_1.game_stats \
    import GameStats
from python_helloworld.section_ii.project_a.chapter_14.example_1.settings \
    import Settings
from python_helloworld.section_ii.project_a.chapter_14.example_1.ship \
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
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                         play_button)


run_game()
