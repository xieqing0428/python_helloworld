# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: settings.py
@time: 2019-01-19 17:28

"""


class Settings:
    """游戏设置"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ufo速度
        self.ufo_speed_factor = 3

        # 子弹设置
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_speed_factor = 1
        self.bullet_allowed = 5
