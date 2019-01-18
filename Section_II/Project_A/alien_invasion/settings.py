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