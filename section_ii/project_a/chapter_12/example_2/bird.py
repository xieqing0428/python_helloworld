# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: bird.py
@time: 2019-01-18 21:48

"""
import pygame


class Bird:
    """创建一个类，将该角色绘制到屏幕中央，并将该图像的背景色设置为屏幕背景色"""
    def __init__(self, screen):
        self.screen = screen

        # 加载图像 获取外矩形
        self.image = pygame.image.load('example_2/images/bird.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
