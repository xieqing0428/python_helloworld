# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_11_02.py
@time: 2019-01-14 15:17

11-2 人口数量：
修改前面的函数，使其包含第三个必不可少的形参population，
并返回一个格式为City, Country - population xxx的字符串，
如Santiago, Chile - population 5000000。
运行test_cities.py，确认测试test_city_country()未通过。

修改上述函数，将形参population设置为可选的。
再次运行test_cities.py，确认测试test_city_country()又通过了。

再编写一个名为test_city_country_population()的测试，
核实可以使用类似于'santiago'、'chile'和'population=5000000'这样的值来调用这个函数。
再次运行test_cities.py，确认测试test_city_country_population()通过了。

"""
import unittest
from HelloWorld.Section_I.Chapter_11.Example.city_functions_plus import \
    city_country, \
    city_country_now, city_country_population


class TestCityFunctionsCase(unittest.TestCase):
    """测试city_functions功能"""

    def test_city_country(self):
        result = city_country('Santiago', 'Chile')
        self.assertEqual(result, "Santiago, Chile")

    def test_city_country_now(self):
        result = city_country_now('Santiago', 'Chile')
        self.assertEqual(result, "Santiago, Chile - population 5000000")

    def test_city_country_population(self):
        result = city_country_population('Santiago', 'Chile', 5000000)
        self.assertEqual(result, "Santiago, Chile - population 5000000")


if __name__ == '__main__':
    unittest.main()
