# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: ship.py
@time: 2019-01-18 17:13

负责管理飞船的大部分行为

"""
import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('example_2/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # 在center属性中存储小数
        self.center = float(self.rect.centery)

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
        self.rect.centery = self.center

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
