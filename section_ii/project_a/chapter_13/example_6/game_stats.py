# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: game_stats.py
@time: 2019-01-21 15:32

"""


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ball_settings):
        """初始化统计信息"""
        self.ball_settings = ball_settings
        # 游戏刚启动时处于活动状态
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.hands_left = self.ball_settings.hand_limit