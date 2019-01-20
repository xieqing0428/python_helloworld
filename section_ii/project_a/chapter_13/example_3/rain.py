# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: rain.py
@time: 2019-01-20 13:00

"""
import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    """雨滴基本设置"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('example_3/images/rain.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        self.rect.y += self.ai_settings.rain_drop_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
