# -*- coding:utf-8 -*-

"""

@author: Alessa0
@file: 9-4.py
@time: 2019-01-12 16:54

9-4 就餐人数：
在为完成练习9-1而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
根据这个类创建一个名为restaurant的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数

"""


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name, type, number_served"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印前述两项信息"""
        print("餐馆的名字叫" + self.restaurant_name.title())
        print("餐馆的烹调类别是" + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + "正在营业")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print("就餐人数为" + str(self.number_served))

    def increment_number_served(self, increment_number):
        self.number_served += increment_number
        print("该餐馆可能接待的就餐人数为" + str(self.number_served))


restaurant = Restaurant('KFC', 'Fried Chicken')
print(str(restaurant.number_served))
restaurant.number_served = 100
print(str(restaurant.number_served))

restaurant.set_number_served(101)
restaurant.increment_number_served(1)

