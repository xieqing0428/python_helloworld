# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: hand.py
@time: 2019-01-18 17:13

负责管理手掌的大部分行为

"""
import pygame
from pygame.sprite import Sprite


class Hand(Sprite):

    def __init__(self, ball_settings, screen):
        """初始化手掌并设置其位置"""
        super().__init__()
        self.screen = screen
        self.ball_settings = ball_settings

        # 加载手掌图像并获取外接矩形
        self.image = pygame.image.load('example_5/images/hand.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新手掌放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在center属性中存储小数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ball_settings.hand_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ball_settings.hand_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制手掌"""
        self.screen.blit(self.image, self.rect)
