# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: game_stats.py
@time: 2019-01-21 11:40

游戏统计信息

"""


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        # 游戏刚启动时处于活动状态
        self.game_active = False

        self.reset_stats()
        # 在任何情况下都不应重置最高得分
        with open(ai_settings.score_store_filename, 'r') as score_file:
            self.high_score = int(score_file.read())

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
