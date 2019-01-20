# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: settings.py
@time: 2019-01-20 12:34

"""


class Settings:

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 雨滴设置
        self.rain_drop_speed = 1
        # 允许新建雨滴对象（用于超出屏幕范围后删除对象及新建对象）
        self.rain_create_allowed = False

