# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: ball.py
@time: 2019-01-20 13:00

"""
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """外星人基本设置"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('example_1/images/star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
