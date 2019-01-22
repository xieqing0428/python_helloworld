# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: game_functions.py
@time: 2019-01-18 21:10

存储大量让游戏《外星人入侵》运行的函数

"""
import sys
from time import sleep

import pygame

from python_helloworld.section_ii.project_a.chapter_14.example_6.alien \
    import Alien
from python_helloworld.section_ii.project_a.chapter_14.example_6.bullet \
    import Bullet


def check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                      aliens, bullets, mouse_x, mouse_y, alien_bullets, rectangle):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        sb.prep_images()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        rectangle.center_rectangle()


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
                 bullets, alien_bullets, rectangle):
    """相应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open(ai_settings.score_store_filename, 'w') as score_file:
                score_file.write(str(stats.high_score))
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y,
                              alien_bullets, rectangle)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, rectangle)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship, rectangle)


def check_keydown_events(event, ai_settings, screen, ship, bullets, rectangle):
    """响应按键"""
    # ai_settings, screen, ship用于创建子弹对象
    # bullets 子弹加入编组
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
        rectangle.moving_right = True
    if event.key == pygame.K_LEFT:
        # 向右移动飞船
        ship.moving_left = True
        rectangle.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship, rectangle):
    """响应松键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        rectangle.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
        rectangle.moving_left = False


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                  play_button, alien_bullets, rectangle):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien_bullet in alien_bullets.sprites():
        alien_bullet.draw_bullet()
    ship.blitme()
    rectangle.draw_rectangle()
    aliens.draw(screen)
    # 显示得分
    sb.show_score()
    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    if len(aliens) == 0:
        # 删除现有的所有子弹，并创建一个新的外星人群
        bullets.empty()
        alien_bullets.empty()
        ai_settings.increase_speed()

        # 提高等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
                                  aliens, bullets, alien_bullets, rectangle):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    hitted = pygame.sprite.spritecollideany(ship, alien_bullets)
    protected = pygame.sprite.spritecollideany(rectangle, alien_bullets)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets,
                    alien_bullets)

    if hitted:
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets,
                 alien_bullets, rectangle)
    if protected:
        alien_bullets.remove(protected)


def check_ship_near_alien(ai_settings, screen, ship, alien, alien_bullets):
    if alien.rect.centerx == ship.rect.centerx:
        fire_bullet(ai_settings, screen, alien, alien_bullets, False)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets,
                   alien_bullets, rectangle):
    for alien in aliens.sprites():
        check_ship_near_alien(ai_settings, screen, ship, alien, alien_bullets)
    bullets.update()
    alien_bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for alien_bullet in alien_bullets.copy():
        if alien_bullet.rect.top >= ai_settings.screen_height:
            alien_bullets.remove(alien_bullet)
        # 检查是否有子弹击中了外星人
        # 如果是这样，就删除相应的子弹和外星人
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
                                  aliens, bullets, alien_bullets, rectangle)


def fire_bullet(ai_settings, screen, ship, bullets, mark=True):
    """开火"""
    if len(bullets) < ai_settings.bullet_allowed:
        # 创建子弹对象
        new_bullet = Bullet(ai_settings, screen, ship, mark)
        # 加入到编组中
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """获得x方向的外星人可放数量"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """新建单个外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         3 * alien_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    for number_row in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, number_row)


def change_fleet_direction(ai_settings, aliens):
    """碰撞屏幕改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    """检查碰撞屏幕"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets,
             alien_bullets, rectangle):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1

        # 更新记分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        rectangle.center_rectangle()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens,
                        bullets, alien_bullets, rectangle):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets,
                     alien_bullets, rectangle)
            break


def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets,
                  alien_bullets, rectangle):
    """更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets,
                 alien_bullets, rectangle)
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens,
                        bullets, alien_bullets, rectangle)


def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
