# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: game_functions.py
@time: 2019-01-18 21:10

存储大量让游戏《外星人入侵》运行的函数

"""
import sys

import pygame

from python_helloworld.section_ii.project_a.chapter_14.example_2.bullet \
    import Bullet


def start_game(stats, ship, rectangle, bullets):
    """
    将check_play_button()的一些代码提取出来，
    放到一个名为start_game()的函数中，
    并在check_play_button()和check_keydown_events()中调用这个函数
    """
    # 隐藏光标
    pygame.mouse.set_visible(False)
    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True

    # 清空子弹列表
    bullets.empty()

    # 创建一群新的外星人，并让飞船居中
    rectangle.center_rectangle()
    ship.center_ship()


def check_play_button(stats, play_button, ship, rectangle, bullets, mouse_x,
                      mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(stats, ship, rectangle, bullets)


def check_events(ai_settings, screen, stats, play_button, ship, rectangle,
                 bullets):
    """相应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, ship, rectangle, bullets,
                              mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    # ai_settings, screen, ship用于创建子弹对象
    # bullets 子弹加入编组
    if event.key == pygame.K_UP:
        # 向上移动飞船
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        # 向下移动飞船
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """响应松键"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ai_settings, screen, stats, ship, rectangle, bullets,
                  play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    rectangle.draw_rectangle()
    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def check_bullet_rectangle_collisions(stats, rectangle, bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    if pygame.sprite.spritecollideany(rectangle, bullets):
        stats.hits_left -= 1
        bullets.empty()
        if stats.hits_left > 0:
            pass
        else:
            stats.game_active = False
            pygame.mouse.set_visible(True)


def update_bullets(stats, rectangle, bullets):
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.left >= rectangle.screen_rect.right:
            bullets.remove(bullet)
        # 检查是否有子弹击中了外星人
        # 如果是这样，就删除相应的子弹和外星人
    check_bullet_rectangle_collisions(stats, rectangle, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """开火"""
    if len(bullets) < ai_settings.bullet_allowed:
        # 创建子弹对象
        new_bullet = Bullet(ai_settings, screen, ship)
        # 加入到编组中
        bullets.add(new_bullet)


def update_rectangle(ai_settings, rectangle):
    rectangle.update()
    """检查碰撞屏幕"""
    if rectangle.check_edges():
        ai_settings.rectangle_direction *= -1
