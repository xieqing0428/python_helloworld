# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: game_functions.py
@time: 2019-01-20 12:56

"""
import sys
from random import randint

import pygame

from python_helloworld.section_ii.project_a.chapter_13.example_5.ball import \
    Ball


def get_number_ball_x(ball_settings, ball_width):
    available_space_x = ball_settings.screen_width - 2 * ball_width
    number_ball_x = int(available_space_x / (2 * ball_width))
    return number_ball_x


def create_ball(ball_settings, screen, balls):
    ball = Ball(ball_settings, screen)
    ball_width = ball.rect.width
    number_ball = get_number_ball_x(ball_settings, ball_width)
    random_number = randint(0, number_ball)
    ball.x = ball_width + 2 * ball_width * random_number
    ball.rect.x = ball.x
    ball.rect.y = ball.rect.height
    balls.add(ball)


def check_events(hand):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, hand)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, hand)


def check_keydown_events(event, hand):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        hand.moving_right = True
    if event.key == pygame.K_LEFT:
        # 向右移动飞船
        hand.moving_left = True


def check_keyup_events(event, hand):
    """响应松键"""
    if event.key == pygame.K_RIGHT:
        hand.moving_right = False
    if event.key == pygame.K_LEFT:
        hand.moving_left = False


def update_screen(ball_settings, screen, hand, balls):
    screen.fill(ball_settings.bg_color)
    hand.blitme()
    balls.draw(screen)
    pygame.display.flip()


def update_balls(ball_settings, screen, hands, balls):
    """更新球的位置"""
    balls.update()
    # 删除消失的球
    for ball in balls.copy():
        if ball.rect.bottom >= ball_settings.screen_height:
            balls.remove(ball)
            # create_ball(ball_settings, screen, balls)
    check_bullet_alien_collisions(ball_settings, screen, hands, balls)


def check_bullet_alien_collisions(ball_settings, screen, hands, balls):
    """响应手掌和球的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(balls, hands, True, False)

    if len(balls) == 0:
        # 删除现有的所有子弹，并创建一个新的外星人群
        balls.empty()
        create_ball(ball_settings, screen, balls)
