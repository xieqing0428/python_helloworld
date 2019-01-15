# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: Exercise_09_02.py
@time: 2019-01-12 15:35

9-2 三家餐馆：
根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant()

"""


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name, type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印前述两项信息"""
        print("餐馆的名字叫" + self.restaurant_name.title())
        print("餐馆的烹调类别是" + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + "正在营业")


restaurant_kfc = Restaurant('KFC', 'Fried Chicken')
restaurant_haidilao = Restaurant('海底捞', '火锅')
restaurant_yonghe = Restaurant('永和豆浆', '快餐')

restaurant_kfc.describe_restaurant()
restaurant_haidilao.describe_restaurant()
restaurant_yonghe.describe_restaurant()

