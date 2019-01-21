# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: rectangle.py
@time: 2019-01-19 20:32

"""
import pygame


class Rectangle:
    """外星人基本设置"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.rectangle_width,
                                ai_settings.rectangle_height)
        self.screen_rect = self.screen.get_rect()

        self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery

        self.y = float(self.rect.y)
        self.color = self.ai_settings.rectangle_color

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        if self.rect.bottom >= self.screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True

    def update(self):
        self.y += self.ai_settings.rectangle_speed_factor * \
                  self.ai_settings.rectangle_direction
        self.rect.y = self.y

    def draw_rectangle(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_rectangle(self):
        """让飞船在屏幕上居中"""
        self.rect.centery = self.screen_rect.centery
