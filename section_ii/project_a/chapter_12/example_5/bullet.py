# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: bullet.py
@time: 2019-01-19 17:28

"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ufo_settings, screen, ufo):
        super().__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ufo_settings.bullet_width,
                                ufo_settings.bullet_height)
        self.rect.centery = ufo.rect.centery
        self.rect.right = ufo.rect.right

        # 存储用小数表示的子弹位置
        self.x = float(self.rect.x)

        self.color = ufo_settings.bullet_color
        self.speed_factor = ufo_settings.bullet_speed_factor

    def update(self):
        """更新子弹位置"""
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """绘制子弹位置"""
        pygame.draw.rect(self.screen, self.color, self.rect)



