# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_12_03.py
@time: 2019-01-19 15:00

12-3 火箭：
编写一个游戏，开始时屏幕中央有一个火箭，而玩家可使用四个方向键上下左右移动火箭。
请务必确保火箭不会移到屏幕外面

"""
import pygame
import python_helloworld.section_ii.project_a.chapter_12.example_3\
    .game_functions as gf
from python_helloworld.section_ii.project_a.chapter_12.example_3.settings \
    import Settings
from python_helloworld.section_ii.project_a.chapter_12.example_3.rocket \
    import Rocket


def run_game():
    """开启游戏"""
    # 模块初始化
    pygame.init()
    # 导入游戏设置
    rocket_settings = Settings()
    # 开启游戏屏幕
    screen = pygame.display.set_mode((rocket_settings.screen_width,
                                     rocket_settings.screen_height))
    # 设置游戏标题
    pygame.display.set_caption("Rocket")

    # 创建游戏对象
    rocket = Rocket(rocket_settings, screen)

    # 主循环
    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(rocket_settings, screen, rocket)

run_game()
