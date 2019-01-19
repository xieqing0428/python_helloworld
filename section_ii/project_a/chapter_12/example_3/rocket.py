# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: rocket.py
@time: 2019-01-19 15:21

"""
import pygame


class Rocket:
    """火箭相关"""

    def __init__(self, rocket_settings, screen):
        # 初始化火箭设置及屏幕
        self.rocket_settings = rocket_settings
        self.screen = screen
        self.LIMITED = 16

        # 加载图像及设置外形
        self.image = pygame.image.load('example_3/images/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 火箭初始化位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - self.LIMITED

        # 移动像素小数化
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # 移动标志
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_up and self.rect.top > self.LIMITED:
            self.bottom -= self.rocket_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom - \
                self.LIMITED:
            self.bottom += self.rocket_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > self.LIMITED:
            self.center -= self.rocket_settings.rocket_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right - \
                self.LIMITED:
            self.center += self.rocket_settings.rocket_speed_factor
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
