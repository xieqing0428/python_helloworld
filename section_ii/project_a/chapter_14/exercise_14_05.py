# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_14_05.py
@time: 2019-01-22 10:28

14-5 重构：
找出执行了多项任务的函数和方法，对它们进行重构，以让代码高效而有序。
例如，对于check_bullet_alien_collisions()，
将其中在外星人群被消灭干净时开始新等级的代码移到一个名为start_new_level()的函数中；
又比如，对于Scoreboard的方法__init__()，
将其中调用四个不同方法的代码移到一个名为prep_images()的方法中，以缩短方法__init__()。
如果你重构了check_play_button()，
方法prep_images()也可为check_play_button()或start_game()提供帮助

"""
import pygame
from pygame.sprite import Group

import python_helloworld.section_ii.project_a.chapter_14.example_5\
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_14.example_5.button \
    import Button
from python_helloworld.section_ii.project_a.chapter_14.example_5.game_stats \
    import GameStats
from python_helloworld.section_ii.project_a.chapter_14.example_5.scoreboard \
    import Scoreboard
from python_helloworld.section_ii.project_a.chapter_14.example_5.settings \
    import Settings
from python_helloworld.section_ii.project_a.chapter_14.example_5.ship \
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
