# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: ufo.py
@time: 2019-01-19 17:28

"""
import pygame


class UFO:
    """UFO对象"""

    def __init__(self, ufo_settings, screen):
        # 屏幕及ufo设置
        self.ufo_settings = ufo_settings
        self.screen = screen
        self.LIMITED = 16

        # ufo图像及rect设置
        self.image = pygame.image.load('example_5/images/ufo.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 初始化飞船位置
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left + self.LIMITED

        # 小数表示ufo位置
        self.centery = float(self.rect.centery)

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """移动位置"""
        if self.moving_up and self.rect.top > self.LIMITED:
            self.centery -= self.ufo_settings.ufo_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom -\
                self.LIMITED:
            self.centery += self.ufo_settings.ufo_speed_factor
        self.rect.centery = self.centery

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
