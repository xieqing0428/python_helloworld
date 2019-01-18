# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: ship.py
@time: 2019-01-18 17:13

负责管理飞船的大部分行为

"""
import pygame


class Ship:

    def __init__(self, screen):
        """初始化飞船并设置其位置"""
        self.screen = screen

        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load(
            'helloworld/section_ii/project_a/alien_invasion/images/ship.bmp')

        