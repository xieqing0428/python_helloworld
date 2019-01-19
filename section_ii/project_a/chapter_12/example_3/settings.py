# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: settings.py
@time: 2019-01-19 15:14

"""


class Settings:
    """存储火箭游戏设置"""

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 火箭设置
        self.rocket_speed_factor = 5
