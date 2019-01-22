# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_14_04.py
@time: 2019-01-22 09:19

14-4 历史最高分：
每当玩家关闭并重新开始游戏《外星人入侵》时，最高分都将被重置。
请修复这个问题，
调用sys.exit()前将最高分写入文件，并当在GameStats中初始化最高分时从文件中读取它

"""
import pygame
from pygame.sprite import Group

import python_helloworld.section_ii.project_a.chapter_14.example_4\
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_14.example_4.button \
    import Button
from python_helloworld.section_ii.project_a.chapter_14.example_4.game_stats \
    import GameStats
from python_helloworld.section_ii.project_a.chapter_14.example_4.scoreboard \
    import Scoreboard
from python_helloworld.section_ii.project_a.chapter_14.example_4.settings \
    import Settings
from python_helloworld.section_ii.project_a.chapter_14.example_4.ship \
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
    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建子弹编组
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens,
                             bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


run_game()
