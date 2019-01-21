# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_13_05.py
@time: 2019-01-20 22:54

13-5 抓球：
创建一个游戏，在屏幕底端放置一个玩家可左右移动的角色。
让一个球出现在屏幕顶端，且水平位置是随机的，并让这个球以固定的速度往下落。
如果角色与球发生碰撞（表示将球抓住了），就让球消失。
每当角色抓住球或球因抵达屏幕底端而消失后，都创建一个新球

"""
import pygame
import python_helloworld.section_ii.project_a.chapter_13.example_5\
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_13.example_5.settings \
    import Settings
from pygame.sprite import Group
from python_helloworld.section_ii.project_a.chapter_13.example_5.hand import \
    Hand


def run_game():
    pygame.init()
    ball_settings = Settings()
    screen = pygame.display.set_mode((ball_settings.screen_width,
                                      ball_settings.screen_height))
    pygame.display.set_caption("ball")

    hand = Hand(ball_settings, screen)
    hands = Group()
    hands.add(hand)
    balls = Group()

    gf.create_ball(ball_settings, screen, balls)

    while True:
        gf.check_events(hand)
        hand.update()
        gf.update_balls(ball_settings, screen, hands, balls)
        gf.update_screen(ball_settings, screen, hand, balls)


run_game()
