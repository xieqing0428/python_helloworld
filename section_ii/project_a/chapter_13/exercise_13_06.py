# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_13_06.py
@time: 2019-01-20 22:54

13-5 抓球：
13-6 游戏结束：
在为完成练习13-5而编写的代码中，跟踪玩家有多少次未将球接着。
在未接着球的次数到达三次后，结束游戏

"""
import pygame
from pygame.sprite import Group

import python_helloworld.section_ii.project_a.chapter_13.example_6 \
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_13.example_6.game_stats \
    import GameStats
from python_helloworld.section_ii.project_a.chapter_13.example_6.hand import \
    Hand
from python_helloworld.section_ii.project_a.chapter_13.example_6.settings \
    import Settings


def run_game():
    pygame.init()
    ball_settings = Settings()
    screen = pygame.display.set_mode((ball_settings.screen_width,
                                      ball_settings.screen_height))
    pygame.display.set_caption("ball")

    hand = Hand(ball_settings, screen)
    hands = Group()
    hands.add(hand)

    stats = GameStats(ball_settings)
    balls = Group()

    gf.create_ball(ball_settings, screen, balls)

    while True:
        gf.check_events(hand)
        if stats.game_active:
            hand.update()
            gf.update_balls(ball_settings, screen, stats, hands, balls)
        gf.update_screen(ball_settings, screen, hand, balls)


run_game()
