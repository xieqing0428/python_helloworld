# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: settings.py
@time: 2019-01-18 16:37

用于将所有设置存储在一个地方，以免在代码中到处添加设置

"""


class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 7

        # 子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 30
        self.bullet_height = 6
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 1

        # 矩形设置
        self.rectangle_speed_factor = 6
        self.rectangle_width = 30
        self.rectangle_height = 90
        self.rectangle_color = (120, 120, 120)
        self.hits_limit = 3

        # fleet_direction为1表示向右移，为-1表示向左移
        self.rectangle_direction = 1
