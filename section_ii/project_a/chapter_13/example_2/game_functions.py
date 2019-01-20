# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: game_functions.py
@time: 2019-01-20 12:56

"""
import sys
from random import randint

import pygame

from python_helloworld.section_ii.project_a.chapter_13.example_2.star import \
    Star


def get_number_star_x(star_settings, star_width):
    available_space_x = star_settings.screen_width - 2 * star_width
    number_star_x = int(available_space_x / (2 * star_width))
    return number_star_x


def get_number_rows(star_settings, star_height):
    available_space_y = star_settings.screen_height - 2 * star_height
    number_star_y = int(available_space_y / (2 * star_height))
    return number_star_y


def create_star(star_settings, screen, stars, number_star, number_row):
    star = Star(star_settings, screen)
    star_width = star.rect.width
    star.x = star_width + 2 * star_width * number_star
    star.rect.x = star.x
    star.rect.y = star.rect.height + 2 * star.rect.height * number_row
    stars.add(star)


def create_fleet(star_settings, screen, stars):
    star = Star(star_settings, screen)
    number_stars_x = get_number_star_x(star_settings, star.rect.width)
    number_rows = get_number_rows(star_settings, star.rect.height)

    for number_row in range(number_rows):
        for number_star in range(number_stars_x):
            random_number = randint(-10, 10)
            if random_number > 0:
                create_star(star_settings, screen, stars, number_star,
                            number_row)


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(star_settings, screen, stars):
    screen.fill(star_settings.bg_color)
    stars.draw(screen)
    pygame.display.flip()
