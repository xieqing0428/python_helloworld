# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: exercise_16_07.py
@time: 2019-01-25 17:02

16-7 测试函数draw_line：
我们编写函数draw_line时，没有使用测试方法检验它能否正确工作。
请利用你在第11章学到的知识，为这个函数编写合适的测试程序

"""
import json
import pygal
import unittest

from python_helloworld.section_ii.project_b.chapter_16.exercise_16_06 import \
    draw_line


class TestDrawLineCase(unittest.TestCase):
    """测试city_functions功能"""

    def test_draw_line(self):

        c_codes = ["ARB"]
        c_names = ["Arab World"]
        values = [25760683041.0857]
        years = [1968]

        result = draw_line(years, values, 'GDP', 'Values')

        line_chart = pygal.Line()
        line_chart.title = 'GDP'
        line_chart.x_labels = years
        line_chart.add('Values', values)
        # line_chart.render_to_file('GDP.svg')

        self.assertEqual(result.title, line_chart.title)


if __name__ == '__main__':
    unittest.main()
