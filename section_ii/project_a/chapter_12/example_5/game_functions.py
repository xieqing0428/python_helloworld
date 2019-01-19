# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: game_functions.py
@time: 2019-01-19 17:29

"""
import sys
import pygame
from python_helloworld.section_ii.project_a.chapter_12.example_5.bullet \
    import Bullet


def check_events(ufo_settings, screen, ufo, bullets):
    """检查按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ufo_settings, screen, ufo, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ufo)


def fire_bullet(ufo_settings, screen, ufo, bullets):
    """开火"""
    if len(bullets) < ufo_settings.bullet_allowed:
        new_bullet = Bullet(ufo_settings, screen, ufo)
        bullets.add(new_bullet)


def check_keydown_events(event, ufo_settings, screen, ufo, bullets):
    """按键"""
    if event.key == pygame.K_UP:
        ufo.moving_up = True
    if event.key == pygame.K_DOWN:
        ufo.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ufo_settings, screen, ufo, bullets)


def check_keyup_events(event, ufo):
    """起键"""
    if event.key == pygame.K_UP:
        ufo.moving_up = False
    if event.key == pygame.K_DOWN:
        ufo.moving_down = False


def update_screen(ufo_settings, screen, ufo, bullets):
    """更新屏幕"""
    screen.fill(ufo_settings.bg_color)
    # 更新子弹位置
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ufo.blitme()
    # 绘制屏幕
    pygame.display.flip()


def update_bullet(ufo, bullets):
    """过界子弹消失"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.left >= ufo.screen_rect.right:
            bullets.remove(bullet)

