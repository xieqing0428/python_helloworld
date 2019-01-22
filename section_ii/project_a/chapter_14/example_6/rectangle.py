# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: rectangle.py
@time: 2019-01-19 20:32

"""
import pygame


class Rectangle:
    """外星人基本设置"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ship.rect.width, 30)
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.centery - 60

        self.center = float(self.rect.centerx)
        self.color = self.ai_settings.rectangle_color

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def draw_rectangle(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_rectangle(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
