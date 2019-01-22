# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_14_06.py
@time: 2019-01-22 11:21

14-6 扩展游戏《外星人入侵》：
想想如何扩展游戏《外星人入侵》。
例如，
可让外星人也能够向飞船射击，
或者添加盾牌，让飞船躲到它后面，使得只有从两边射来的子弹才能摧毁飞船。
另外，还可以使用像pygame.mixer这样的模块来添加音效，如爆炸声和射击声

"""
import pygame
from pygame.sprite import Group

import python_helloworld.section_ii.project_a.chapter_14.example_6\
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_14.example_6.button \
    import Button
from python_helloworld.section_ii.project_a.chapter_14.example_6.game_stats \
    import GameStats
from python_helloworld.section_ii.project_a.chapter_14.example_6.scoreboard \
    import Scoreboard
from python_helloworld.section_ii.project_a.chapter_14.example_6.settings \
    import Settings
from python_helloworld.section_ii.project_a.chapter_14.example_6.ship \
    import Ship
from python_helloworld.section_ii.project_a.chapter_14.example_6.rectangle \
    import Rectangle


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(ai_settings, screen)
    rectangle = Rectangle(ai_settings, screen, ship)
    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建子弹编组
    bullets = Group()
    alien_bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets, alien_bullets, rectangle)
        if stats.game_active:
            ship.update()
            rectangle.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets, alien_bullets, rectangle)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens,
                             bullets, alien_bullets, rectangle)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button, alien_bullets, rectangle)


run_game()

