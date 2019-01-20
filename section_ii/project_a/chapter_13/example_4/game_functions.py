# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: game_functions.py
@time: 2019-01-20 12:56

"""
import sys
from random import randint

import pygame

from python_helloworld.section_ii.project_a.chapter_13.example_4.rain import \
    Rain


def get_number_rain_x(rain_settings, rain_width):
    available_space_x = rain_settings.screen_width - 2 * rain_width
    number_rain_x = int(available_space_x / (2 * rain_width))
    return number_rain_x


def get_number_rows(rain_settings, rain_height):
    available_space_y = rain_settings.screen_height - 2 * rain_height
    number_rain_y = int(available_space_y / (2 * rain_height))
    return number_rain_y


def create_rain(rain_settings, screen, rains, number_rain, number_row):
    rain = Rain(rain_settings, screen)
    rain_width = rain.rect.width
    rain.x = rain_width + 2 * rain_width * number_rain
    rain.rect.x = rain.x
    rain.rect.y = rain.rect.height + 2 * rain.rect.height * number_row
    rains.add(rain)


def create_fleet(rain_settings, screen, rains, single=False):
    rain = Rain(rain_settings, screen)
    number_rains_x = get_number_rain_x(rain_settings, rain.rect.width)
    if single:
        number_rows = 1
    else:
        number_rows = get_number_rows(rain_settings, rain.rect.height)

    for number_row in range(number_rows):
        for number_rain in range(number_rains_x):
            random_number = randint(-10, 10)
            if random_number > 0:
                create_rain(rain_settings, screen, rains, number_rain,
                            number_row)


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(rain_settings, screen, rains):
    screen.fill(rain_settings.bg_color)
    rains.draw(screen)
    pygame.display.flip()


def update_rains(rain_settings, screen, rains):
    """更新雨群中所有雨滴的位置"""
    rains.update()
    # 删除消失的雨滴

    for rain in rains.copy():
        if rain.rect.top >= rain_settings.screen_height:
            rains.remove(rain)
            rain_settings.rain_create_allowed = True
        else:
            # 防止重复新建雨滴对象
            if rain_settings.rain_create_allowed:
                create_fleet(rain_settings, screen, rains, single=True)
                rain_settings.rain_create_allowed = False
